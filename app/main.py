from fastapi import FastAPI
import uvicorn
from app.recommender import MovieRecommender

recommender = MovieRecommender(
    "data/tmdb_5000_movies.csv",
    "data/tmdb_5000_credits.csv",
    "data/ratings.csv"
)

app = FastAPI()

@app.get("/recommend/{user_id}/{movie_title}")
def recommend(user_id: int, movie_title: str):
    return {"recommendations": recommender.hybrid_recommend(user_id, movie_title)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
