import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np

class DeepRecommender:
    def __init__(self, num_users, num_movies, embedding_size=50):
        self.model = self.build_model(num_users, num_movies, embedding_size)

    def build_model(self, num_users, num_movies, embedding_size):
        model = Sequential([
            Embedding(num_users, embedding_size, input_length=1),
            LSTM(128, activation='relu'),
            Dense(64, activation='relu'),
            Dense(num_movies, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, user_movie_data, labels, epochs=5, batch_size=32):
        self.model.fit(user_movie_data, labels, epochs=epochs, batch_size=batch_size)

    def recommend(self, user_id):
        predictions = self.model.predict(np.array([user_id]))
        return np.argsort(predictions[0])[-10:][::-1]
