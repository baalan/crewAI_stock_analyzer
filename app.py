import warnings
import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from IPython.display import Markdown

load_dotenv()

warnings.filterwarnings('ignore')

llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")


data_scraper = Agent(
    role="data scraper",
    goal="Scrape data from multiple websites for stock {stock}",
    backstory="You're working on stock data collection "
              "about the stock: {stock}."
              "You collect information that helps the "
              "audience learn something "
              "and make informed decisions. "
              "Your work is the basis for "
              "the data colector and make action according to that",
    allow_delegation=False,
	verbose=True
)

plan = Task(
    description=(
        "1. Prioritize the latest trends, key news, "
            "and noteworthy news on stock {stock}.\n"
        "2. Identify the growth of the sector, considering "
            "people needs.\n"
        "3. Develop a detailed analysis."
    ),
    expected_output="A comprehensive content plan document "
        "with an outline, stock analysis, "
        "Inovation done by the company and impact on the community",
    agent=data_scraper,
)

crew = Crew(
    agents=[data_scraper],
    tasks=[plan],
    verbose=2
)

result = crew.kickoff(inputs={"stock": "Infosys"})

Markdown(result)