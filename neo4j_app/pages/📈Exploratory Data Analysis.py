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

st.header("Exploratory Data Analysis 🕵️‍♂️")
file_path = os.getcwd() + '/Summer22_FootballTransfers.csv'
data = pd.read_csv(file_path)
st.write(data)

unique_countries = pd.unique(data[['country_origin_club', 'country_new_club']].values.ravel('K'))
unique_countries = pd.DataFrame(unique_countries, columns=['Country'])
#st.write(unique_countries)

countries_with_long_lat = pd.read_csv(os.getcwd() + '/countries_with_longlat.csv').rename(columns={'name':'Country'})

#st.write(countries_with_long_lat)
countries_df = unique_countries.merge(countries_with_long_lat, on='Country', how='left').dropna()
#st.write(countries_df)

st.subheader('Map to display the distribution of teams that made transfers')
st.map(data=countries_df, color='#E0B0FF')
#st.write(data['country_new_club'])
country_count = data['country_new_club'].value_counts().reset_index().rename(columns={'country_new_club':'Country', 'count':'No of Players'})

#st.write(country_count)
st.bar_chart(data=country_count, y='No of Players', x='Country', color=['#E0B0FF'])

st.subheader("Number of players by position")
position_count = data['position'].value_counts().reset_index().rename(columns={'count':'Count', 'position':'Position'})
st.bar_chart(data=position_count, x='Position', y='Count', color=['#E0B0FF'])


bins = [0, 20, 30, 40, 100]
labels = ['0-20', '21-30', '31-40', '41+']
data['Age Group'] = pd.cut(data['age'], bins=bins, labels=labels, right=False)

data['player_value'] = data['player_value'].str.replace('€', '')
data['player_value'] = data['player_value'].str.replace('Th.', 'e3')
data['player_value'] = data['player_value'].str.replace('m', 'e6')
data['player_value'] = pd.to_numeric(data['player_value'], errors='coerce')

# data['cost'] = data['cost'].str.replace('Loan fee:€', '')  
# data['cost'] = data['cost'].str.replace('€', '')            
# data['cost'] = data['cost'].str.replace('Th.', 'e3')        
# data['cost'] = data['cost'].str.replace('m', 'e6')          
# data['cost'] = pd.to_numeric(data['cost'], errors='coerce')

#grouped_df = data.agg({'cost':'mean', 'player_value':'mean'})
st.subheader("Average player value in each age group")

data['player_value'] = pd.to_numeric(data['player_value'])
grouped_df = data.groupby('Age Group').agg({'player_value':'mean'}).rename(columns={'player_value': 'Player Value'}).reset_index()
st.line_chart(data=grouped_df, y='Player Value',x='Age Group', color=['#E0B0FF'])

