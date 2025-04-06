from crewai import Agent, Task, Crew, LLM, Process
from dotenv import load_dotenv
import os
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()

# Initialize LLM
llm = LLM(
    model="gemini/gemini-2.0-flash-lite-001", # Gemini 2.0 Flash-Lite
    api_key = os.getenv("GEMINI"),
    max_tokens = 500,
    temperature = 0.7
)

# Define agents
researcher = Agent(
    role="Research Analyst",
    goal="Gather information on news topics based on your knowledge",
    backstory="""You are a knowledgeable research analyst who uses your extensive understanding of current events
              to provide insights on news topics. You rely on your knowledge to summarize key information.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

summarizer = Agent (
    role = "Content Summarizer",
    goal = "Create concise summaries with key takeaways",
    backstory = """You are a professional content curator who excels at distilling complex information into clear, 
                concise summaries. You can identify the most important points and present them clearly.""",
    verbose = True,
    allow_delegation = False,
    llm = llm
    )

