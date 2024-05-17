"""File for performing RAG using Neo4J."""

# IMPORTS --------------------------------------------------------------------------------------------------------------

import os

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph

# ENVIRONMENT VARIABLES ------------------------------------------------------------------------------------------------

_ = load_dotenv()

api_key = os.getenv("AZURE_OPENAI_KEY")
api_version = os.getenv("AZURE_OPENAI_VERSION")
api_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

neo_url = os.getenv("URL")
neo_username = os.getenv("NEO4J_USERNAME")
neo_password = os.getenv("NEO4J_PASSWORD")

# FUNCTIONS ------------------------------------------------------------------------------------------------------------

def run_llm_graph_rag(query: str) -> str:
    """Performs RAG using Neo4j as context.

    Arguments:
        query (str): The question to ask the LLM.

    Returns:
        str: Answer to the input query.
    """
    graph = Neo4jGraph(url=neo_url, username=neo_username, password=neo_password)
    graph.refresh_schema()

    model = AzureChatOpenAI(model="genai00-gpt-35-turbo-0613", api_key=api_key, api_version=api_version)
    chain = GraphCypherQAChain.from_llm(graph=graph, llm=model)

    return  '\n' + chain.invoke({"query": query})['result'] + '\n'
