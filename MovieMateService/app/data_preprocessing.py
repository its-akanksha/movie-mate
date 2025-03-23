import pandas as pd

class DataPreprocessor:
    def __init__(self, movies_path, credits_path, ratings_path):
        self.movies_path = movies_path
        self.credits_path = credits_path
        self.ratings_path = ratings_path

    def load_and_process_data(self):
        movies = pd.read_csv(self.movies_path)
        credits = pd.read_csv(self.credits_path)
        ratings = pd.read_csv(self.ratings_path)

        movies = movies.merge(credits, on='title')
        movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
        movies.dropna(inplace=True)
        movies['metadata'] = movies['genres'] + " " + movies['keywords'] + " " + movies['cast']
        movies['metadata'] = movies['metadata'].apply(lambda x: x.split())

        return movies, ratings
