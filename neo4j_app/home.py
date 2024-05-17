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
    
    We decided to focus on the following algorithms:
    
    👩‍💻 **Dijkstra's Algorithm:** finds the shortest path between nodes in a graph

    👩‍💻 **Node Similarity:** a measure to determine how similar or related two nodes are based on various characteristics (uses the Jaccard Similarity Score)
    """
)
st.image('jaccard.png')

file_path = os.getcwd() + '/Summer22_FootballTransfers.csv'
data = pd.read_csv(file_path)
#st.write(data)

unique_countries = pd.unique(data[['country_origin_club', 'country_new_club']].values.ravel('K'))
unique_countries = pd.DataFrame(unique_countries, columns=['Country'])
#st.write(unique_countries)

countries_with_long_lat = pd.read_csv(os.getcwd() + '/countries_with_longlat.csv').rename(columns={'name':'Country'})

#st.write(countries_with_long_lat)
countries_df = unique_countries.merge(countries_with_long_lat, on='Country', how='left').dropna()
#st.write(countries_df)

st.subheader('Map to display the distribution of teams')
st.map(data=countries_df)


st.subheader("Number of players by position")
position_count = data['position'].value_counts().reset_index()
st.bar_chart(data=position_count, x='position', y='count')

st.subheader("Algorithm Search")
player1 = st.selectbox('Select your first player', data['name'], placeholder='Choose player')
player2 = st.selectbox('Select your second player', data['name'], placeholder='Choose player')

if player1 and player2:
    st.write(run_dijkstra(players=[player1, player2], driver=set_driver()))
    st.write(run_similarity(players=[player1, player2], driver=set_driver()))

