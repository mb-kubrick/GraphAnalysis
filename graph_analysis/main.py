"""File for running full graph analysis on the supplied data."""

# IMPORTS --------------------------------------------------------------------------------------------------------------

import argparse

from louvain import run_louvain
from similarity import run_similarity
from degree_centrality import run_degree_centrality
from build import set_driver, close_driver, build_graph, read_data

# MAIN APP -------------------------------------------------------------------------------------------------------------

def main() -> None:
    """Function to run main app."""
    driver = set_driver()
    raw_data = read_data()
    graph = build_graph(raw_data)
    louvain_result = run_louvain(graph)
    similarity_result = run_similarity(graph)
    degree_centrality_result = run_degree_centrality(graph)
    close_driver(driver)

# Run the main function
if __name__ == "__main__":
    main()
