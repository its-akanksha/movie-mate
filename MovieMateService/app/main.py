from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from recommender import MovieRecommender

recommender = MovieRecommender(
    "data/tmdb_5000_movies.csv",
    "data/tmdb_5000_credits.csv",
    "data/ratings.csv"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to the Movie Recommender API"}

@app.get("/recommend/{user_id}/{movie_title}")
def recommend(user_id: int, movie_title: str):
    try:
        recommendations = recommender.hybrid_recommend(user_id, movie_title)
        
        if not recommendations:
            raise HTTPException(status_code=404, detail="No recommendations found")
        
        return {"recommendations": recommendations}

    except IndexError:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.get("/movies")
def get_all_movies():
    try:
        all_movies = recommender.get_all_movie_titles()
        
        return {"movies": all_movies}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching movies: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)