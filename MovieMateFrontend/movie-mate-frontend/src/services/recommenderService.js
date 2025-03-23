import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const getRecommendations = async (userId, movieTitle) => {
  try {
    const response = await axios.get(`${API_URL}/recommend/${userId}/${encodeURIComponent(movieTitle)}`);
    console.log("RESPONSE:", response);
    return response.data.recommendations;
  } catch (error) {
    console.error("Error fetching recommendations:", error);
    return [];
  }
};

export const getAllMovies = async () => {
  try {
    const response = await axios.get(`${API_URL}/movies`);
    return response.data.movies;
  } catch (error) {
    console.error("Error fetching all movies:", error);
    return [
      "The Shawshank Redemption", "The Godfather", "The Dark Knight",
      "Pulp Fiction", "Fight Club", "Forrest Gump", "Inception",
      "The Matrix", "Goodfellas", "The Silence of the Lambs",
      "Star Wars", "The Lord of the Rings", "Interstellar",
      "Gladiator", "The Avengers", "Jurassic Park", "Titanic",
      "Avatar", "The Lion King", "Toy Story", "Finding Nemo"
    ];
  }
};

export const getMovieDetails = async (movieId) => {
  try {
    const response = await axios.get(`${API_URL}/movie/${movieId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching movie details:", error);
    return null;
  }
};