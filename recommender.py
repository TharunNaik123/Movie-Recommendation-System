import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
def __init__(self, data_path):
self.movies = pd.read_csv(data_path)
self._clean_data()
self._vectorize()


def _clean_data(self):
# Replace missing genres
self.movies['genres'] = self.movies['genres'].replace('(no genres listed)', '')
# Convert genres to space-separated text
self.movies['genres'] = self.movies['genres'].str.replace('|', ' ', regex=False)
self.movies['title_clean'] = self.movies['title'].str.lower()


def _vectorize(self):
self.tfidf = TfidfVectorizer(stop_words='english')
self.tfidf_matrix = self.tfidf.fit_transform(self.movies['genres'])
self.similarity_matrix = cosine_similarity(self.tfidf_matrix)


def recommend(self, movie_title, top_n=5):
movie_title = movie_title.lower()
if movie_title not in self.movies['title_clean'].values:
return "Movie not found in dataset"


idx = self.movies[self.movies['title_clean'] == movie_title].index[0]
scores = list(enumerate(self.similarity_matrix[idx]))
scores = sorted(scores, key=lambda x: x[1], reverse=True)
top_movies = scores[1:top_n+1]


return [self.movies.iloc[i]['title'] for i, _ in top_movies]
