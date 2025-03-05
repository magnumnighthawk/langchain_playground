from langchain_core.messages import HumanMessage, SystemMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import MessagesState, StateGraph, START
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    max_new_tokens=512, temperature=0.8)
chat = ChatHuggingFace(llm=llm, verbose=True)

messages = [
    HumanMessage("Hi. I'm Blue from India"),
    HumanMessage("Tell me something nice about my country")
]

workflow = StateGraph(state_schema=MessagesState)

def call_model(state: MessagesState):
    response = chat.invoke(state['messages'])
    return {'messages': response}

workflow.add_edge(START, "model")
workflow.add_node('model', call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}

response = app.invoke({'messages': [messages[0]]}, config)
print(response["messages"][-1])

response = app.invoke({'messages': [messages[1]]}, config)
print(response["messages"][-1])