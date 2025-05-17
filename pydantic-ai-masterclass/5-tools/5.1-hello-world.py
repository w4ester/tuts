import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
import secrets

load_dotenv()

# Define the model
model = OpenAIModel('gpt-4o-mini', api_key=os.getenv('OPENAI_API_KEY'))

def roll_die() -> str:
    """Roll a six-sided die and return the result."""
    return str(secrets.SystemRandom().randint(1, 6))

# Define the agent
agent = Agent(model=model, tools=[roll_die])
result = agent.run_sync('My guess is 4')
print(result.data)
