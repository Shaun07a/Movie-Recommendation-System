import pandas as pd
import pickle
import ast

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

# Merge datasets
movies = movies.merge(credits, on="title")

# Select required columns
movies = movies[['movie_id',
                 'title',
                 'overview',
                 'genres',
                 'keywords',
                 'cast',
                 'crew']]

movies.dropna(inplace=True)


# --------------------------
# Helper Functions
# --------------------------

def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L


def convert_cast(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L


def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L


# Convert JSON columns
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert_cast)
movies['crew'] = movies['crew'].apply(fetch_director)

movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Remove spaces
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

# Create tags column
movies['tags'] = (
    movies['overview'] +
    movies['genres'] +
    movies['keywords'] +
    movies['cast'] +
    movies['crew']
)

# Keep only useful columns
new_df = movies[['movie_id', 'title', 'tags']]

# Convert list into string
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

# Lowercase
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(new_df['tags']).toarray()

# Cosine similarity
similarity = cosine_similarity(vectors)

# Save files
pickle.dump(new_df.to_dict(), open("movie_dict.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

print("Movie dictionary saved.")
print("Similarity matrix saved.")