from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.exa import ExaTools
from agno.models.groq import Groq
from agno.workflow import Step , Workflow , Parallel
from agno.agent import Agent

load_dotenv()

exa = ExaTools()

llm = Groq(id = "llama-3.1-8b-instant" )


amazon_agent = Agent(
    model = llm,
    id = "Amazon Agent",
    name = "Amazon Agent",
    tools = [exa],
    markdown=True,
    instructions=["You are a great web searcher for amazon website",
                  "You have to find the price of the given object from amazon.",
                  "You have the acces to the duck duck go search tool"]
)

flipkart_agent = Agent(
    model = llm,
    id = "Flipkart Agent",
    name = "Flipkart Agent",
    tools = [exa],
    instructions=["You are a great web searcher for flipkart",
                  "You have to find the price of the given object from flipkart",
                  "You have the access for the brave search tool"]
)

summarizer = Agent(
    model = llm,
    id = "Summarize",
    name = "Summarize",
    markdown=True,
    stream=True,
    instructions=["You are a great summarizer",
                  "summarize the whole data a good heading"]
)

step1 = Step(
    name = "Step 1 ",
    agent = amazon_agent,
    description="To find the price of the object from the amazon website"
)

step2 = Step(
    name = "Step 2",
    agent = flipkart_agent,
    description="To find the price of the given object from flipkart"
)

step3 = Step(
    name = "Step 3",
    agent = summarizer,
    description="To summarize the entire data with a good heading"
)

parallel = Parallel(
    step1 , step2,
    name = "parallel workflow",
    description="parallel workflow to find the price of the product from both website"
)

workflow = Workflow(
    id = "Workflow",
    name = "Workflow",
    description="To find the price from multiple website and then give the summary",
    steps = [parallel , step3],
)

workflow.print_response(input="My product is Vivo x300 pro",
                        markdown=True,
                        stream = True)