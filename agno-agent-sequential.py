from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.workflow import Step , Workflow
from agno.tools.duckduckgo import DuckDuckGoTools

# To search the tourist places in the given city and then finding the distance to each spot from the users house


load_dotenv()

llm = Groq(id = "llama-3.1-8b-instant")

search = DuckDuckGoTools()
search2 = DuckDuckGoTools()

places_finder_agent = Agent(
    model = llm,
    id = "places_finder",
    name = "places finder",
    markdown=True,
    instructions=["You are a great tourist agent",
                  "Your work is to find the tourist places near the mentioned place by the user",
                  "You have the access to the search tool , you can search the web for finding places."],
    tools=[search]
)

distances_finder_agent = Agent(
    model = llm,
    id = "distance_finder",
    name = "distance finder",
    instructions = ["You are the great distance finder",
                    "You need to find the distance from the place where user live currently to every tourist places.",
                    "You have the access to the searching tool"],
    markdown=True,
    tools = [search2]
)

summarizer_agent = Agent(
    model = llm,
    id = "summarizer",
    name = "summarize everything",
    markdown=True,
    instructions=["You are great summarizer",
                  "You need to summarize everything and give in a proper format."]
)


# Build a step

step1 = Step(
    name = "find the places",
    agent=places_finder_agent,
    description="The work is to find the best tourist places near the place given by " \
    "the user"
)

step2 = Step(
    name = "find the distance",
    agent= distances_finder_agent,
    description="The work is to find the distance from the user living area to each " \
    "tourist place"
)

step3 = Step(
    name = "summarize everything",
    agent= summarizer_agent,
    description="The work is to summarize everything and return the answer in a proper" \
    "format"
)

workflow = Workflow(
    id = "Sequential Worflow",
    description="Sequential workflow for trip planning",
    steps = [step1 , step2 , step3],
)


workflow.print_response(input="""I currently live in mumbai , and i am planning to trip in pune.
                        so help me with that"""
                        , markdown=True,
                        stream=True)


