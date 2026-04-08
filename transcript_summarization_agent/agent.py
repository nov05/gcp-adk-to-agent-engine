import os
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.models import Gemini
from google.genai import types

RETRY_OPTIONS = types.HttpRetryOptions(initial_delay=1, max_delay=3, attempts=30)

load_dotenv()

root_agent = Agent(
    name="transcript_summarization_agent",
    description="Summarizes chat transcripts.",
    model=Gemini(
        model=os.getenv("MODEL", "gemini-2.5-flash"),
        retry_options=RETRY_OPTIONS
    ),
    instruction="Summarize the provided chat transcript.",
)