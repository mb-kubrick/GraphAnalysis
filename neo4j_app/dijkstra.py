"""Code to run the Dijkstra algorithm on the graph dataset."""

# IMPORTS --------------------------------------------------------------------------------------------------------------

import os
import numpy as np

# FUNCTIONS ------------------------------------------------------------------------------------------------------------

def run_dijkstra(players, driver) -> str:
    """Determines the shortest path between nodes.

    Args:
        players (list): List of players that currently exist within the graph.
        driver (driver): The driver instance which is connected to Neo4j.

    Returns:
        str: The shortest path between players, as a string.
    """

    player_1, player_2 = np.random.choice(players, replace=False, size=2)

    folder_path = os.getcwd() + '/cypher/'

    file_names = ['dijkstra_clean.cypher', 'dijkstra_build.cypher', 'dijkstra_call.cypher']
    all_params = [{}, {}, {'player_1_name': player_1, 'player_2_name': player_2}]

    for file_name, params in zip(file_names, all_params):

        with open(folder_path + file_name, "r", encoding='utf-8') as file:
            query = file.read()

        with driver.session() as session:
            result = session.run(query, **params).data()

    raw_path_data = result[0]['path']

    return (f"\nThe shortest connection from '{player_2}' to '{player_1}' is:"
            + f"\n{' -> '.join([i['name'] for i in raw_path_data])}\n")
