import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=d8aa000f7efb99bd0210da5444af1fbe&language=en-US".format(movie_id)
    response = requests.get(url) # enter api key
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x:x[1])[1:6]

    recommeded_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        # print(movies.iloc[i[0]].title)
        movie_id = movies.iloc[i[0]].movie_id
        # fetch posster 
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommeded_movies.append(movies.iloc[i[0]].title)
    return recommeded_movies, recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# movies_list = movies_list['title'].values
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

option = st.selectbox('Type or select a movie name', movies['title'].values)

if st.button('Show recommendation'):
    # recommendations = recommend(option)
    # for i in recommendations:
    #     st.write(i)
    names, posters = recommend(option)
    col1, col2, col3, col4, col5 = st.beta_coloumns(3)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    