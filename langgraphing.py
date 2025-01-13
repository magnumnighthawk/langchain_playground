import json
from typing import Annotated
from typing_extensions import TypedDict

from langchain_core.messages import ToolMessage

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

class State(TypedDict):
    messages: Annotated[list, add_messages]

  
graph_builder = StateGraph(State)

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

# Basic tool calling node
class BasicToolNode:
    def __init__(self, tools: list) -> None:
        self.tools_by_name = {tool.name: tool for tool in tools}
        
    def __call__(self, inputs: dict):
        if messages := inputs.get('messages', []):
            message = messages[-1]
        else:
            raise ValueError("No message found in input")
    
        outputs = []
        for tool_call in message.tool_calls:
            tool_result = self.tools_by_name[tool_call['name']].invoke(tool_call['args'])
            outputs.append(ToolMessage(content=json.dumps(tool_result), name=tool_call['name'], tool_call_id=tool_call['id']))
    
        return {'messages': outputs}

def route_tools(state: State):
    if isinstance(state, list):
        ai_message = state[-1]
    elif messages := state.get('messages', []):
        ai_message = messages[-1]
    else:
        raise ValueError(f"No messages found in input state to tool_edge: {state}")
    
    if hasattr(ai_message, 'tool_calls') and len(ai_message.tool_calls) > 0:
        return 'tools'
    return END

tool_node = BasicToolNode(tools=tools)

graph_builder.add_node('chatbot', chat)
graph_builder.add_node('tools', tool_node)
graph_builder.add_edge(START, 'chatbot')
graph_builder.add_conditional_edges('chatbot', route_tools, {'tools': 'tools', END: END})
graph_builder.add_edge('tools', 'chatbot')


graph = graph_builder.compile()

def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [("user", user_input)]}):
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