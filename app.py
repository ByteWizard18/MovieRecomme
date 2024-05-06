import streamlit as st
import pickle
import pandas as pd



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].title

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

with bz2.BZ2File('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

st.title('Movie Recommender System')

option = st.selectbox('What would you like to watch sir?',movies['title'].values)

if st.button('Recommend'):
    names = recommend(option)
    col1, _ = st.columns(2)
    with col1:
        for name in names:
            st.text(name)
