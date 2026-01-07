from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.in_memory import InMemoryDb

load_dotenv()

llm = Groq(id = "llama-3.1-8b-instant")

db = InMemoryDb()

agent = Agent(
    model = llm,
    db = db,
    session_id="session1",
    add_history_to_context=True,
    num_history_runs=3,
    name = "My First Agno Agent",
    markdown=True,
    stream = True
)

agent.print_response("Write the 200 word paragraph about the Gen AI.")

agent.print_response("About what topic i asked you earlier.")

