import datetime
import os
import asyncio
import warnings
import logging

from google.genai import types # For creating message Content/Parts
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm # For multi-model support
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner


# Ignore all warnings
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)

os.environ["OPENAI_API_KEY"]
MODEL_GPT_4O_MINI = "gpt-4o-mini"


# Define the tools
def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city (e.g., "New York", "London", "Tokyo").

    Returns:
        dict: A dictionary containing the weather information.
              Includes a 'status' key ('success' or 'error').
              If 'success', includes a 'report' key with weather details.
              If 'error', includes an 'error_message' key.
    """
    # Best Practice: Log tool execution for easier debugging
    city_normalized = city.lower().replace(" ", "") # Basic input normalization

    # Mock weather data for simplicity
    mock_weather_db = {
        "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
        "london": {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
        "tokyo": {"status": "success", "report": "Tokyo is experiencing light rain and a temperature of 18°C."},
    }

    # Best Practice: Handle potential errors gracefully within the tool
    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}


# print(get_weather("New York"))
# print(get_weather("Paris"))


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


# Define the Agent
# @title Define Agent Interaction Function

async def call_agent_async(query: str, runner: Runner, user_id: str, session_id: str):
  """Sends a query to the agent and prints the final response."""
  print(f"\n>>> User Query: {query}")

  content = types.Content(role='user', parts=[types.Part(text=query)])
  final_response_text = "Agent did not produce a final response."

  # Key Concept: run_async executes the agent logic and yields Events.
  # We iterate through events to find the final answer.
  async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
      # Key Concept: is_final_response() marks the concluding message for the turn.
      if event.is_final_response():
          if event.content and event.content.parts:
             # Assuming text response in the first part
             final_response_text = event.content.parts[0].text
          elif event.actions and event.actions.escalate: # Handle potential errors/escalations
             final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          # Add more checks here if needed (e.g., specific error codes)
          break # Stop processing events once the final response is found

  print(f"<<< Agent Response: {final_response_text}")


try:
    weather_agent_gpt = Agent(
        name="weather_time_agent",
        model=LiteLlm(model=MODEL_GPT_4O_MINI),
        description=("Agent to answer questions about the time and weather in a city."),
        instruction="You are a helpful weather assistant powered by GPT-4o. "
                    "Use the 'get_weather' tool for city weather requests. "
                    "Clearly present successful reports or polite error messages based on the tool's output status.",
        tools=[get_weather, get_current_time],
    )

    print(f"Agent '{weather_agent_gpt.name}' created using model '{MODEL_GPT_4O_MINI}'.")

    # InMemorySessionService is simple, non-persistent storage for this tutorial.
    session_service_gpt = InMemorySessionService()

    # Define constants for identifying the interaction context
    APP_NAME = "weather_tutorial_app"
    USER_ID_GPT = "user_1"
    SESSION_ID_GPT = "session_001"

    # Create the specific session where the conversation will happen
    session_gpt = session_service_gpt.create_session(
        app_name=APP_NAME,
        user_id=USER_ID_GPT,
        session_id=SESSION_ID_GPT
    )
    print(f"Session created: App='{APP_NAME}', User='{USER_ID_GPT}', Session='{SESSION_ID_GPT}'")

    # Create a runner specific to this agent and its session service
    runner_gpt = Runner(
        agent=weather_agent_gpt,
        app_name=APP_NAME,
        session_service=session_service_gpt # Uses our session manager
    )
    print(f"Runner created for agent '{runner_gpt.agent.name}'.")
    
except Exception as e:
    print(f"❌ Could not create or run GPT agent '{MODEL_GPT_4O_MINI}'. Check API Key and model name. Error: {e}")


# Run the conversation
# @title Run the Initial Conversation
# We need an async function to await our interaction helper
async def run_conversation():

    # Ensure call_agent_async uses the correct runner, user_id, session_id
    await call_agent_async("What is the weather like in London?",
                     runner=runner_gpt,
                     user_id=USER_ID_GPT,
                     session_id=SESSION_ID_GPT)
    
# Execute the conversation using await in an async context (like Colab/Jupyter)

if __name__ == "__main__":
    # Run the event loop
    asyncio.run(run_conversation())
