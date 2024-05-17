"""Functions for building the graph."""

# IMPORTS --------------------------------------------------------------------------------------------------------------

import os
import json
from dotenv import load_dotenv
from neo4j import GraphDatabase

# FUNCTIONS ------------------------------------------------------------------------------------------------------------

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

def connection_test(driver):
    try:
        return driver.verify_authentication()
    except Exception as e:
        print(f'Failed to connect to driver, reason: {e}')

def close_driver(driver):
    """Closes the supplied driver."""
    driver.close()

def read_data():
    file_path = r'C:\Football Exercise\GraphAnalysis\data\Summer22_FootballTransfers.json'

    with open(file_path, "r", encoding='utf-8') as file:
        data = json.load(file)

    return data

def build_graph(driver, raw_data, n_items = 100):
    """Builds the graph from the supplied JSON data."""
    folder_path = os.getcwd() + '/graph_analysis/cypher/'
    file_names = ['clean_database.cypher', 'build.cypher']

    params_per_file = [{},
                       {'player_names': raw_data['name'][:n_items],
                        'positions': raw_data['position'][:n_items],
                        'ages': raw_data['age'][:n_items],
                        'origin_clubs': raw_data['origin_club'][:n_items],
                        'league_origin_clubs': raw_data['league_origin_club'][:n_items],
                        'country_origin_clubs': raw_data['country_origin_club'][:n_items],
                        'new_clubs': raw_data['new_club'][:n_items],
                        'league_new_clubs': raw_data['league_new_club'][:n_items],
                        'country_new_clubs': raw_data['country_new_club'][:n_items],
                        'player_names': raw_data['name'][:n_items],
                        }]

    for file_name, params in zip(file_names, params_per_file):
        with open(folder_path + file_name, "r", encoding='utf-8') as file:
            query = file.read()

        with driver.session() as session:
            result = session.run(query, **params)