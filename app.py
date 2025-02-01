import streamlit as st
import pandas as pd

data = pd.read_csv('data.csv')

st.title("Welcome to the Restaurant Recommendation System")
st.write("Here you will get a recommendation of restaurant and recommendations will be based on Price and Cuisine")

st.write("I used cosine similarity technique to find the similarity between restaurants")

name = st.selectbox("Select the Restaurant you like", data['Name'].unique().tolist())

recs = (data[['Name',name]].sort_values(by=name, ascending=False)
        .head(10))

st.write("Here are your top 10 recommendation based on your selected restaurant")

st.dataframe(recs)