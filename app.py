import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('Pickle_Files_Used_by_app.py\movies_dict.pkl','rb'))
movies_list = pd.DataFrame(movies_dict)
# st.write(movies_list)
# movies_list= movies_list['title'].values
similarity = pickle.load(open('Pickle_Files_Used_by_app.py\similarity.pkl','rb'))



def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_scores = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    similar_list=[]
    movie_posters = []
    for i in movies_scores:
        #print(movies_list.iloc[i[0]].title)
        movie_id = movies_list.iloc[i[0]].movie_id
        similar_list.append(movies_list.iloc[i[0]].title)
        #movie_posters.append()
        
    return similar_list
st.title("Movie Recommender")




option = st.selectbox(
    "Select your movie",
    movies_list['title'].values
)

st.write("You selected:", option)


if st.button("Recommend", type="primary"):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)