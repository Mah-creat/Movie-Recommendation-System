import pandas as pd
import pickle
import streamlit as st
import requests
import os

# Function to fetch posters from TMDB API
def fetch_poster(movie_id):
    # Fixed URL: Added '/3/movie/' correctly and ensured proper formatting
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        # Poster path needs to be appended to the base image URL
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return "https://via.placeholder.com/150"
    except Exception:
        # Fallback image if API fails or connection is lost
        return "https://via.placeholder.com/150"

# Function to recommend movies
def recommend(selected_movie):
    # Find the index of the selected movie
    # movie_index = movies[movies['title'] == movie].index[0]
    # distances = similarity[movie_index]
    
    # # Sort similarity scores and pick top 5 (excluding the movie itself)
    # # Using key=lambda x: x[1] to sort by similarity score
    # movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # recommended_movie_names = []
    # recommended_movie_posters = []

    # for i in movies_list:
    #     # i[0] is the index, i[1] is the similarity score
    #     idx = i[0]
    #      # Access columns safely using ['column_name']
    
    #     temp_movie_id = movies.iloc[idx]['movie_id']

    # recommended_movie_names.append(movies.iloc[idx]['title'])
    # recommended_movie_posters.append(fetch_poster(temp_movie_id))

    # return recommended_movie_names, recommended_movie_posters

    try:
        # Find index of selected movie
        movie_index = movies[movies['title'] == selected_movie].index[0]
        distances = similarity[movie_index]

        # Get top 5 similar movies (excluding selected movie)
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movie_names = []
        recommended_movie_posters = []

        for i in movies_list:
            idx = i[0]
            # # Access movie_id and title correctly
            # temp_movie_id = movies.iloc[idx]['movie_id']
            # recommended_movie_names.append(movies.iloc[idx]['title'])
            # recommended_movie_posters.append(fetch_poster(temp_movie_id))
            # Safely access movie_id
            if 'movie_id' in movies.columns:
                temp_movie_id = movies.iloc[idx]['movie_id']
                recommended_movie_posters.append(fetch_poster(temp_movie_id))
            else:
                # fallback if movie_id missing
                recommended_movie_posters.append("https://via.placeholder.com/150")

                # Append the title
            recommended_movie_names.append(movies.iloc[idx]['title'])

        return recommended_movie_names, recommended_movie_posters

    except Exception as e:
        st.error(f"Error in recommendation: {e}")
        return [], []

# --- UI Setup ---
st.set_page_config(page_title="Movie Recommender", layout="wide")
# st.header('Movie Recommender System')
st.title("🎬 Movie Recommender System")

# Get the correct directory path for the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the data (Using Cache to prevent slow reloading of large files)
@st.cache_data
def load_data():
    movies_dict_path = os.path.join(current_dir, "model", "movie_dict.pkl")
    similarity_path = os.path.join(current_dir, "model", "similarity.pkl")
    
    # Load dictionary and convert back to DataFrame
    # with open(movies_dict_path, "rb") as f:
    #     movies_dict = pickle.load(f)
    movies = pd.read_pickle(movies_dict_path)
    with open(similarity_path, "rb") as f:  
        similarity_data = pickle.load(f)

      # --- DEBUG: check columns ---
    # st.write("Columns in movies DataFrame:", movies.columns)
    # st.write(movies.head())

    # return pd.DataFrame(movies_dict), similarity_data
    return movies, similarity_data

# Initialize and run the app logic
try:
    movies, similarity = load_data()
    
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        names, posters = recommend(selected_movie)

        # # Use st.columns to display recommendations in a horizontal grid
        # cols = st.columns(5)
        # for idx, col in enumerate(cols):
        #     with col:
        #         st.text(names[idx])
        #         st.image(posters[idx], use_container_width=True)
        if names and posters:
            cols = st.columns(5)
            for idx, col in enumerate(cols):
                with col:
                    st.text(names[idx])
                    st.image(posters[idx], width="stretch")
        else:
            st.info("No recommendations to show.")

                
except FileNotFoundError:
    st.error("Error: Could not find model files. Please move 'movie_dict.pkl' and 'similarity.pkl' into a folder named 'model'.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")