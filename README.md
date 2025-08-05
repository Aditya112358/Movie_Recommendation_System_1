# 🎬 Movie Recommendation System

A content-based movie recommender built with Python and Streamlit, using the TMDB 5000 dataset. It suggests movies based on user-selected titles by analyzing metadata like genres, cast, crew, and keywords.

> 🚀 **Try it locally**: Quickly spin up the app with `streamlit run app.py`.

---

## 📌 Features

- 🔍 Recommend similar movies based on metadata
- 🧠 Uses cosine similarity between processed movie vectors
- 📦 Loads preprocessed data and models from `.pkl` files for fast performance
- 🧹 Data cleaning and feature engineering done in a Jupyter notebook
- 💡 Built with simplicity, performance, and clarity in mind

---

## 🗂️ Folder Structure

### Movies_rec
* data - The data can be downloaded through this link- https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata . The data files couldn't be uploaded because of the large file size but can be accessed from the provided link.
* The two .pkl files: Contains the processed data in `movies_dict.plk` that is used by the app.py to fetch movies and recommend similar movies using `similarity.pkl`.

* app.py - Contains the actual code that wraps the functionality of the recommendation system with a `streamlit` interface. This is the file that the user needs to run with `streamlit run app.py`.

* movie_rec.ipynb - The .ipynb file is collection of experiments done on the data to yield the optimum output. This where the TMDB dataset was preprocessed and our model parameters were trained.

* README.md - Provides an introduction to the project with basic instructions on how to use this.

* requirements.txt - Contains the list of libraries used in the development of this project.




