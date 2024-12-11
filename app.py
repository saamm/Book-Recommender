import pickle
import streamlit as st
import streamlit.web.cli as stcli
from streamlit.web.cli import main
import numpy as np

st.header("Book Recommender System Using Machine Learning")

#necessary pickle files
model = pickle.load(open('model.pkl', 'rb'))
book_name = pickle.load(open('book_name.pkl', 'rb'))
final_rating = pickle.load(open('final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('book_pivot.pkl', 'rb'))

def fetch_poster(suggestion):
    book_name = []
    ids_idx = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_idx.append(ids)

    for idx in ids_idx:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url


#Recommendation function used belo
def recommend_books(book_name):
    booklist = [] #save recommended books
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors = 6)
    #poster url
    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            booklist.append(j)

    return booklist, poster_url


#Selection box
selected_books = st.selectbox(
    "Type or Select a Book",
    book_name
)

if st.button("Show Recommendations for my book"):
    recommendation_books, poster_url = recommend_books(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])

    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])

    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2])

    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3])

    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4])

    with col5:
        st.text(recommendation_books[5])
        st.image(poster_url[5])