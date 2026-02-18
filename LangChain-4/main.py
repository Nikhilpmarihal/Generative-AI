from dotenv import load_dotenv
load_dotenv()

import os
from tavily import TavilyClient
from langchain.tools import tool  
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage


# Initialize Tavily client
tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

@tool
def surfInternet(query: str) -> str:
    """Use this tool for getting the latest information from the internet"""
    result = tavily_client.search(query=query)
    return str(result) 

model = ChatGoogleGenerativeAI(model = "models/gemini-flash-lite-latest")

agent = create_agent(model = model, tools = [surfInternet])

response = agent.invoke({
    "messages":[HumanMessage("Who is the president of the United States?")]
})

print(response)
