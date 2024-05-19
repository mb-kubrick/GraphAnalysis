import streamlit as st
import os
from main import main
from build1 import set_driver
from neo4j import GraphDatabase
from louvain import run_louvain
from similarity import run_similarity
from dijkstra import run_dijkstra
from build1 import set_driver, close_driver, build_graph, read_data, connection_test
import pandas as pd

st.header("Summer 2022 Football Transfer ⚽")
st.write("<span style='font-style: italic;'>Fahima Ahmed, Michael Berney, Mak Dedic, Kiran Hosein, Danielle Hurford, Visahan Sritharan (Pod 1)</span>", unsafe_allow_html=True)

st.markdown(
    """
    The data was downloaded from this Kaggle dataset: [Football Summer Market 2022](https://www.kaggle.com/datasets/davidmolina/football-summer-market-2022)
    
    Reasons for why we chose this dataset:

"""
)   
reasons = st.button('Reasons')

if reasons:
    st.markdown(
        """
    📊 Clean and coherent

    📊 Large dataset

    📊 Complex relationships (player transfers)

    📊 Intuitive Visualization
"""
    )

st.write("We decided to focus on the following algorithms:")

algorithms = st.button('Algorithms')

if algorithms:
    st.markdown("""
                    👩‍💻 **Degree Centrality:** A measure of how important (or central) a node is to a network by computing the number of dependencies the node has.  
         - Identifying key players and clubs
         - Market positioning

         👩‍💻 **Dijkstra's Algorithm:** Finds the shortest path between nodes in a graph.  
         - Player to Player relationships

         👩‍💻 **Louvain Modularity:** Uncovers the community structure in large networks.  
         - Similar transfer patterns

         👩‍💻 **Node Similarity:** A measure to determine how similar or related two nodes are based on various characteristics (uses the Jaccard Similarity Score).  
        - Compare players
         """

                )
    st.image('jaccard.png')



