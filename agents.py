from langchain_community import tools
import inspect
from langchain_openai import ChatOpenAI
from langchain_community.tools import YouTubeSearchTool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
prompt = "Using south indian cuisine, create the perfect protein rich breakfast for a 30 year old male looking to build muscle and lose weight. Suggest some recipes on Youtube and some good blog posts"

youtube_search = YouTubeSearchTool()
tavily_search = TavilySearchResults(max_results=2)

agent = create_react_agent(chat, tools=[youtube_search, tavily_search])
response = agent.invoke({"messages": [HumanMessage(content=prompt)]})

# Print the response in a pretty format
pprint(response["messages"])