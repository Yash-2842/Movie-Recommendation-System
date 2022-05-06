import streamlit as st
import pickle
import pandas as pd
import requests


movie_list = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
# print(movie_list.head())

def recommend(movie):
    index = movie_list[movie_list['title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    title = []
    poster = []
    for i in distances[1:6]:
        movie_id = movie_list.iloc[i[0]].movie_id
        title.append(movie_list.iloc[i[0]].title)
        poster.append(f"https://image.tmdb.org/t/p/w500/{fetch_poster(movie_id)}")
    return title,poster

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=6372a77da2a6c394b04073e963632ac6')
    data = response.json()
    return data['poster_path']

st.title("Movie Recommender System")
selected_movie_name = st.selectbox('Select Movie',movie_list['title'].values)
if st.button('Recommend'):
    movie_name,movie_poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])