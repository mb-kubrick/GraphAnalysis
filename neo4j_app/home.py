import streamlit as st
from main import main
from build1 import set_driver
from neo4j import GraphDatabase
from louvain import run_louvain
from similarity import run_similarity
from dijkstra import run_dijkstra
from build1 import set_driver, close_driver, build_graph, read_data, connection_test
import pandas as pd

data = pd.read_csv(r"C:\Bench\GenAi_training\GraphAnalysis\neo4j_app\Summer22_FootballTransfers.csv")
st.write(data['name'])

player1 = st.selectbox('Select your first player', data['name'])
player2 = st.selectbox('Select your second player', data['name'])

if player1 and player2:
    st.write(run_dijkstra(players=[player1, player2], driver=set_driver()))
    st.write(run_similarity(players=[player1, player2], driver=set_driver()))

