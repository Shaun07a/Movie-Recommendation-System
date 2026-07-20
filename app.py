import streamlit as st
import pickle
import pandas as pd

from helper import recommend

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your favorite ones!")

# Load movie list
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

selected_movie = st.selectbox(
    "Choose a movie",
    movies["title"].values
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for i, movie in enumerate(recommendations, start=1):
        st.write(f"**{i}. {movie}**")