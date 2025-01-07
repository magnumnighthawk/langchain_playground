from langchain_community import tools
import inspect
from langchain_openai import ChatOpenAI
from langchain_community.tools import YouTubeSearchTool
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# NOTE: Doesn't work as expected
def list_available_tools():
    # First, let's see what we have in the tools module
    print("\nExploring tools module content:")
    print("-------------------------")
    for name, obj in inspect.getmembers(tools):
        print(f"{name}: {type(obj)}")

    # Now let's try to find actual tool classes
    print("\nLooking for tool classes:")
    print("-------------------------")
    tool_list = []
    for name, obj in inspect.getmembers(tools):
        if inspect.isclass(obj):
            print(f"Found class: {name}")
            print(f"Attributes: {dir(obj)}\n")
            if hasattr(obj, 'name'):
                tool_list.append(obj.name)
    return tool_list

# Print available tools
# Commenting out as it doesn't work as expected
# print("Available LangChain Community Tools:")
# print("-------------------------")
# tools_found = list_available_tools()
# if tools_found:
#     for tool_name in tools_found:
#         print(f"- {tool_name}")
# else:
#     print("No tools found") 

    
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
prompt = "Using reliable food science and knowledge of South indian cuisine, create the perfect protein rich breakfast for a 30 year old male looking to build muscle and lose weight. Suggest good youtube videos to watch for the recipe."

tool = YouTubeSearchTool()

agent = create_react_agent(llm, tools=[tool])
response = agent.invoke({"messages": [HumanMessage(content=prompt)]})

print(response["messages"])