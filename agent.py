import os
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_openai import OpenAI
import wikipedia

# 🔍 Tool 1: Wikipedia
def wiki_search(query: str) -> str:
    return wikipedia.summary(query, sentences=2)

# ➗ Tool 2: Kalkulačka
def calc_tool(query: str) -> str:
    try:
        result = eval(query)
        return f"Výsledek výpočtu {query} je {result}"
    except Exception as e:
        return f"Chyba ve výpočtu: {str(e)}"

# 📦 Nástroje pro agenta
tools = [
    Tool(
        name="Wikipedia",
        func=wiki_search,
        description="Užitečné pro hledání informací o lidech, místech, věcech, událostech."
    ),
    Tool(
        name="Calculator",
        func=calc_tool,
        description="Slouží k výpočtům, jako je 5 + 8 * 2."
    )
]

# 🧠 Inicializace jazykového modelu
llm = OpenAI(temperature=0)

# 🤖 Vytvoření agenta
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 🔎 Dotazy na agenta
print("\nDotaz 1: Kdo je Jaromír Jágr?")
print(agent.run("Kdo je Jaromír Jágr?"))

print("\nDotaz 2: Kolik je 25 * 4 + 10?")
print(agent.run("Kolik je 25 * 4 + 10?"))
