import pandas as pd
import numpy as np
import time

csv_path = "./data/tmdb_5000_movies.csv"

movies_df = pd.read_csv(csv_path)

movie_ids = movies_df["id"].tolist()

num_users = 1000  
num_ratings = len(movie_ids) * 5  

ratings_data = {
    "userId": np.random.randint(1, num_users + 1, size=num_ratings),
    "movieId": np.random.choice(movie_ids, size=num_ratings, replace=True),
    "rating": np.random.uniform(0, 5, size=num_ratings).round(1),   
}

ratings_df = pd.DataFrame(ratings_data)

ratings_df.to_csv("ratings.csv", index=False)

print("✅ ratings.csv file generated successfully!")
