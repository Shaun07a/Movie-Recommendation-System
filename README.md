# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Python**, **Scikit-learn**, and **Streamlit**. The application recommends movies similar to a selected movie by analyzing movie metadata such as genres, keywords, cast, director, and overview using **Cosine Similarity**.

---

## Features

- Content-based movie recommendations
- Fast and lightweight recommendation engine
- Interactive Streamlit web interface
- Cosine Similarity for finding similar movies
- Offline functionality (No external API required)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## Dataset

This project uses the **TMDB 5000 Movie Dataset**, which contains detailed information about thousands of movies, including:

- Movie Title
- Overview
- Genres
- Keywords
- Cast
- Crew

The recommendation model combines these features to generate personalized movie suggestions.

---

## Project Structure

```
Movie-Recommendation-System/
│
├── app.py
├── helper.py
├── model.py
├── requirements.txt
├── README.md
│
└── data/
    ├── tmdb_5000_movies.csv
    └── tmdb_5000_credits.csv
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Shaun07a/Movie-Recommendation-System.git
```

### Navigate to the project directory

```bash
cd Movie-Recommendation-System
```

### Create a virtual environment

```bash
python -m venv movie
```

### Activate the virtual environment

**Windows**

```bash
movie\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Generate recommendation files

```bash
python model.py
```

This creates:

- `movie_dict.pkl`
- `similarity.pkl`

### Run the application

```bash
streamlit run app.py
```

---

## How It Works

1. Load movie and credits datasets.
2. Merge both datasets.
3. Extract important movie features:
   - Overview
   - Genres
   - Keywords
   - Cast
   - Director
4. Convert textual information into vectors using **CountVectorizer**.
5. Compute similarity scores using **Cosine Similarity**.
6. Recommend the top five most similar movies.

---

## Future Improvements

- Movie posters
- Genre filtering
- Search suggestions
- Hybrid recommendation system
- User ratings integration
- Collaborative filtering

---

## Author

**Shaun Joseph**

