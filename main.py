from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

# from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama
# from langchain_groq import ChatGroq

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# from tavily import TavilyClient
from langchain_tavily import TavilySearch

"""
tavily = TavilyClient()

@tool
def search(query: str) -> str:
    
    #Tool that searches over internet
    #Args:
    #    query: The query to search for
    #Returns:
    #    The search result
    #

    print(f"Searching for {query}")
    return tavily.search(query=query)
"""

llm = ChatOpenAI(model="gpt-5")
# tools = [search]
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")

    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="search for 3 job posted for an ai engineer using langchain in the Plano Texas Area"
            )
        }
    )
    print(result)

    information = """
    Attack on Titan (Japanese: 進撃の巨人, Hepburn: Shingeki no Kyojin; lit. 'The Advancing Giant') is a Japanese manga series written and illustrated by Hajime Isayama. Set in a world where humanity is forced to live in cities surrounded by three enormous walls that protect them from gigantic man-eating humanoids referred to as Titans, the story follows Eren Yeager, an adolescent boy who vows to exterminate the Titans after they bring about the destruction of his hometown and the death of his mother. It was serialized in Kodansha's monthly magazine Bessatsu Shōnen Magazine from September 2009 to April 2021, with its chapters collected in 34 tankōbon volumes.

An anime television series was produced by Wit Studio (seasons 1–3) and MAPPA (season 4). A 25-episode first season was broadcast from April to September 2013, followed by a 12-episode second season broadcast from April to June 2017. A 22-episode third season was broadcast in two parts, with the first 12 episodes airing from July to October 2018 and the last 10 episodes airing from April to July 2019. A fourth and final season premiered in December 2020, airing 16 episodes in its first part. A second part consisting of 12 episodes aired from January to April 2022, and the third and fourth parts aired in two specials; the first premiered in March 2023, and the second premiered in November 2023.

Attack on Titan has been met with critical and commercial success. By November 2023, the manga had over 140 million copies in circulation, making it one of the best-selling manga series of all time. It has won several awards, including the Kodansha Manga Award, the Attilio Micheluzzi Award, and the Harvey Award.
    """

    summary_template = """
    given the information {information} about an anime tv series I want you to create:
    1. A short summary
    2. two interesting facts about the series
"""

    # summary_prompt_template = PromptTemplate(
    #    input_variables=["information"], template=summary_template
    # )

    # llm = ChatOpenAI(temperature=0, model="gpt-5")
    # llm = ChatOllama(temperature=0, model="gemma3:270m")
    # llm = ChatGroq(temperature=0, model="openai/gpt-oss-120b")
    # chain = summary_prompt_template | llm
    # response = chain.invoke(input={"information": information})
    # print(response.content)


if __name__ == "__main__":
    main()
