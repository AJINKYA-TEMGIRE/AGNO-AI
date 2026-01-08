from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from textwrap import dedent

load_dotenv()

llm = Groq(id = "llama-3.1-8b-instant")
web_search = DuckDuckGoTools()

agent = Agent(
    model = llm,
    tools = [web_search],
    markdown=True,
    stream = True,
    instructions=dedent("""
        You are very expert in web search.
        You will recieve the query from the user and you need to answer it by searching on the web for most up to date information.""")
)

agent.print_response("When will Virat kohli play his next match?")

