import json
from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode, tools_condition

# from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)
memory = MemorySaver()

# llm = ChatAnthropic(model="claude-3.5-sonnet-20240620")
llm = ChatOpenAI(model='gpt-3.5-turbo')
tavily_search = TavilySearchResults(
                max_results=2,
                include_answer=True,
                include_raw_content=True,
                include_images=True
            )
tools = [tavily_search]
llm_with_tools = llm.bind_tools(tools)

# Simple chat node
def chat(state: State):
    return {"messages": [llm_with_tools.invoke(state['messages'])]}

tool_node = ToolNode(tools=tools)

graph_builder.add_node('chatbot', chat)
graph_builder.add_node('tools', tool_node)
graph_builder.add_edge(START, 'chatbot')
graph_builder.add_conditional_edges('chatbot', tools_condition)
graph_builder.add_edge('tools', 'chatbot')

graph = graph_builder.compile(checkpointer=memory, interrupt_before=['tools'])
config = {"configurable": {"thread_id": "1"}}

def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [("user", user_input)]}, config, stream_mode="values"):
        for value in event.values():
            print("Assistant:", value["messages"][-1].pretty_print())

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ['quit', 'q', 'exit']:
            print('Goodbye!')
            break
        
        stream_graph_updates(user_input)
    
    except:
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break