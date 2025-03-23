import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from sklearn.decomposition import TruncatedSVD
from data_preprocessing import DataPreprocessor

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

        self.ratings = self.ratings.groupby(['userId', 'movieId'], as_index=False).rating.mean()

        ratings_matrix = self.ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

        self.svd = TruncatedSVD(n_components=min(20, min(ratings_matrix.shape)-1)) 
        self.svd.fit(ratings_matrix)


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

        ratings_matrix = self.ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

        if user_id not in ratings_matrix.index:
            return content_recommendations 

        user_vector = self.svd.transform(ratings_matrix.loc[[user_id]])
        svd_scores = np.dot(user_vector, self.svd.components_)

        svd_recommendations = [
            self.movies[self.movies['movie_id'] == movie_id].title.values[0]
            for movie_id in np.argsort(svd_scores[0])[-10:][::-1]
            if movie_id in self.movies['movie_id'].values
        ]

        hybrid_results = list(set(content_recommendations + svd_recommendations))[:10]
        return hybrid_results

    def get_all_movie_titles(self):
        """Return all movie titles available in the dataset"""
        return self.movies['title'].tolist()
