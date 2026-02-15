# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Machine Learning and Streamlit.  
This application suggests similar movies based on the movie selected by the user.

---

## 🚀 Live Demo
(You can add Streamlit deployment link here later)

---

## 📌 Project Overview

This project recommends movies based on similarity between movie metadata such as:

- Genres
- Keywords
- Cast
- Crew
- Overview

It uses Natural Language Processing techniques and cosine similarity to find related movies.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- TMDB Dataset

---

## 📂 Project Structure

Movie-Recommendation-System
│
├── app.py
├── create_model_files.py
├── movie-recommendation-system.ipynb
├── model/ (ignored in GitHub)
├── README.md

---

## 🧠 How It Works

1. Data preprocessing and feature extraction  
2. Text vectorization using CountVectorizer  
3. Cosine similarity calculation  
4. Recommend top 5 similar movies  
5. Display movie posters using TMDB API  

---

## ⚠️ Note

Model (`.pkl`) files and dataset files are not uploaded to GitHub due to size limitations.

You can regenerate model files by running:

```bash
python create_model_files.py


▶️ How To Run Locally

Clone the repository:
git clone https://github.com/Mah-creat/Movie-Recommendation-System.git

Navigate to project folder:
cd Movie-Recommendation-System

Install dependencies:
pip install -r requirements.txt

Run Streamlit app:
streamlit run app.py

👩‍💻 Author

Pooja Maheshwari

GitHub: https://github.com/Mah-creat