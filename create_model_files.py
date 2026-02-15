import pandas as pd
import numpy as np
import pickle
import os

# --- Load your dataset ---
# Replace 'movies.csv' with your actual dataset
movies_csv_path = "tmdb_5000_movies.csv"
movies = pd.read_csv(movies_csv_path)

# --- Example: compute similarity matrix ---
# For demonstration, let's assume similarity is a dummy matrix
# Replace this with your actual similarity computation
similarity = np.random.rand(len(movies), len(movies))

# --- Create model folder if it doesn't exist ---
current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, "model")
os.makedirs(model_dir, exist_ok=True)

# --- Save movies DataFrame as dictionary ---
# movies_dict = movies.to_dict()
# with open(os.path.join(model_dir, "movie_dict.pkl"), "wb") as f:
#     pickle.dump(movies_dict, f)
movies.to_pickle(os.path.join(model_dir, "movie_dict.pkl"))

# --- Save similarity matrix ---
with open(os.path.join(model_dir, "similarity.pkl"), "wb") as f:
    pickle.dump(similarity, f)

print("✅ .pkl files saved successfully in 'model' folder")
