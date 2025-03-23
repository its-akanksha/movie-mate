import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
from app.data_preprocessing import DataPreprocessor

class MovieRecommender:
    def __init__(self, movies_path, credits_path, ratings_path):
        self.preprocessor = DataPreprocessor(movies_path, credits_path, ratings_path)
        self.movies, self.ratings = self.preprocessor.load_and_process_data()
        self.model = None
        self.svd = None
        self.content_similarity = None
        self.train_models()

    def train_models(self):
        self.model = Word2Vec(sentences=self.movies['metadata'], vector_size=100, window=5, min_count=1, workers=4)
        movie_vectors = np.array([self.get_movie_vector(title) for title in self.movies['title']])
        self.content_similarity = cosine_similarity(movie_vectors)

        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(self.ratings[['userId', 'movieId', 'rating']], reader)
        trainset, _ = train_test_split(data, test_size=0.2)
        self.svd = SVD()
        self.svd.fit(trainset)

    def get_movie_vector(self, title):
        try:
            return np.mean(
                [self.model.wv[word] for word in self.movies[self.movies['title'] == title]['metadata'].values[0] if word in self.model.wv],
                axis=0
            )
        except:
            return np.zeros(100)

    def hybrid_recommend(self, user_id, movie_title):
        try:
            idx = self.movies.index[self.movies['title'] == movie_title].tolist()[0]
        except IndexError:
            return ["Movie not found"]

        similar_movies = list(enumerate(self.content_similarity[idx]))
        similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:11]
        content_recommendations = [self.movies.iloc[i[0]].title for i in similar_movies]

        svd_predictions = [(movie, self.svd.predict(user_id, movie_id).est) for movie_id, movie in zip(self.movies['movie_id'], self.movies['title'])]
        svd_recommendations = sorted(svd_predictions, key=lambda x: x[1], reverse=True)[:10]
        svd_recommendations = [movie for movie, _ in svd_recommendations]

        hybrid_results = list(set(content_recommendations + svd_recommendations))[:10]
        return hybrid_results
