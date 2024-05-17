"""Code to compute the similarity on the graph dataset."""

# IMPORTS --------------------------------------------------------------------------------------------------------------

import os
import numpy as np

# FUNCTIONS ------------------------------------------------------------------------------------------------------------

def run_similarity(players, driver) -> str:
    """Determines the shortest path between nodes.

    Args:
        players (list): List of players that currently exist within the graph.
        driver (driver): The driver instance which is connected to Neo4j.

    Returns:
        int: The Jaccard similarity between players.
    """

    player_1, player_2 = np.random.choice(players, replace=False, size=2)

    folder_path = os.getcwd() + '/graph_analysis/cypher/'

    file_names = ['similarity_clean.cypher', 'similarity_build.cypher', 'similarity_call.cypher']
    all_params = [{}, {}, {'player_1_name': player_1, 'player_2_name': player_2}]

    for file_name, params in zip(file_names, all_params):

        with open(folder_path + file_name, "r", encoding='utf-8') as file:
            query = file.read()

        with driver.session() as session:
            result = session.run(query, **params).data()

    try:
        player_similarity = str(result[0]['similarity'])
    except IndexError:
        player_similarity = "0"


    return (f"\nThe jaccard similarity between '{player_1}' and '{player_2}' is: "
            + f"{player_similarity}")