import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(moive_id):
  response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=64c2e68dd99d05fe37d4663a15278f48&language=en-US".format(moive_id))
  data = response.json()
  return "https://image.tmdb.org/t/p/w500"+ data["poster_path"]

def recommended(movie):   
  
  index_of_movie = movies[movies['title'] == movie].index[0]
  distances = similarity[index_of_movie]
  
  top5 = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

  recommended_movies=[]
  recommended_movies_poster=[]
  for i in top5:
    movie_id = movies.iloc[i[0]].id
    recommended_movies.append(movies['title'][i[0]])
    #fetching poster
    recommended_movies_poster.append(fetch_poster(movie_id))

  return recommended_movies,recommended_movies_poster

movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recomendation System')

option = st.selectbox("Select Your Movie",movies_list)

if st.button("Recommeded"):
  name,poster = recommended(option)
  col1 ,col2 ,col3 ,col4 ,col5 = st.columns(5,gap="medium")
  with col1:
    st.text(name[0])
    st.image(poster[0])
  with col2:
    st.text(name[1])
    st.image(poster[1])
  with col3:
    st.text(name[2])
    st.image(poster[2])
  with col4:
    st.text(name[3])
    st.image(poster[3])
  with col5:
    st.text(name[4])
    st.image(poster[4])

