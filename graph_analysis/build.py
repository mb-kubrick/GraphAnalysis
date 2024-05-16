import os
import json
from dotenv import load_dotenv
from neo4j import GraphDatabase

def build_graph(driver, raw_data):
    file_path = os.getcwd() + '/graph_analysis/cypher/build.cypher'

    with open(file_path, "r", encoding='utf-8') as file:
        query = file.read()

    with driver.session() as session:
        result = session.run(query)

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
    file_path = os.getcwd() + '/data/Summer22_FootballTransfers.json'

    with open(file_path, "r", encoding='utf-8') as file:
        return json.load(file)

def connection_test(driver):
    try:
        return driver.verify_authentication()
    except Exception as e:
        print(f'Failed to connect to driver, reason: {e}')