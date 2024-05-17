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
st.write("<span style='font-style: italic;'>Pod 1</span>", unsafe_allow_html=True)
file_path = os.getcwd() + '/Summer22_FootballTransfers.csv'
data = pd.read_csv(file_path)
st.write(data)

unique_countries = pd.unique(data[['country_origin_club', 'country_new_club']].values.ravel('K'))
unique_counties = pd.DataFrame(unique_countries, columns=['Country'])
st.write(unique_countries)

countries_with_long_lat = pd.read_csv(os.getcwd() + '/countries_with_longlat.csv',)
countries_df = unique_countries.merge(countries_with_long_lat, on='name', how='left')
st.write(countries_with_long_lat)


player1 = st.selectbox('Select your first player', data['name'])
player2 = st.selectbox('Select your second player', data['name'])

if player1 and player2:
    st.write(run_dijkstra(players=[player1, player2], driver=set_driver()))
    st.write(run_similarity(players=[player1, player2], driver=set_driver()))

