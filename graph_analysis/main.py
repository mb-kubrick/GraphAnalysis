"""File for running full graph analysis on the supplied data."""

# IMPORTS --------------------------------------------------------------------------------------------------------------

import argparse

from louvain import run_louvain
from similarity import run_similarity
from dijkstra import run_dijkstra
from build import set_driver, close_driver, build_graph, read_data, connection_test

# MAIN APP -------------------------------------------------------------------------------------------------------------

def main() -> None:
    """Function to run main app."""
    driver = set_driver()
    connection_test(driver)
    raw_data = read_data()
    players = build_graph(driver, raw_data)
    # louvain_result = run_louvain(graph)
    # similarity_result = run_similarity(graph)
    print(run_dijkstra(players, driver))
    close_driver(driver)

if __name__ == "__main__":
    main()
