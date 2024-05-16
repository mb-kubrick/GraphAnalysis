import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

def build_graph():
    return

def set_driver():
    """Defines the Neo4j Connection driver.

    Returns:
        driver: The driver used to connect to the database.
    """
    _ = load_dotenv()
    url = os.getenv("URL")
    username = os.getenv("NEO4J_USERNAME")
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(url, auth=(username, password))
    return driver

def close_driver(driver):
    """Closes the supplied driver."""
    driver.close()

def read_data():
    return