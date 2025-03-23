import React, { useState, useContext, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { MovieContext } from "../context/MovieContext";
import MovieList from "./MovieList";
import "./Home.css";

const Home = () => {
  const [userId, setUserId] = useState(1);
  const [movieTitle, setMovieTitle] = useState("");
  const [isExpanded, setIsExpanded] = useState(false);
  const searchInputRef = useRef(null);
  const navigate = useNavigate();
  const { allMovies, loading } = useContext(MovieContext);

  const handleSearch = () => {
    if (movieTitle.trim()) {
      navigate(`/recommendations/${userId}/${encodeURIComponent(movieTitle)}`);
    } else {
      searchInputRef.current.focus();
      searchInputRef.current.classList.add("shake");
      setTimeout(() => {
        searchInputRef.current.classList.remove("shake");
      }, 500);
    }
  };

  const handleMovieSelect = (movie) => {
    setMovieTitle(movie);
  };

  return (
    <div className="home-container">
      <div className={`movie-list-panel ${isExpanded ? "expanded" : ""}`}>
        <div className="panel-toggle" onClick={() => setIsExpanded(!isExpanded)}>
          <i className={`fas fa-chevron-${isExpanded ? "left" : "right"}`}></i>
        </div>
        <h3>Available Movies</h3>
        <MovieList movies={allMovies} loading={loading} onSelectMovie={handleMovieSelect} />
      </div>

      <div className="search-container">
        <div className="search-card">
          <h1>Find Your Next Favorite Movie</h1>
          <p>Get personalized movie recommendations based on your preferences</p>
          
          <div className="input-group">
            <label>User ID</label>
            <input
              type="number"
              value={userId}
              onChange={(e) => setUserId(e.target.value)}
              min="1"
              className="user-input"
            />
          </div>
          
          <div className="input-group">
            <label>Movie Title</label>
            <input
              ref={searchInputRef}
              type="text"
              value={movieTitle}
              onChange={(e) => setMovieTitle(e.target.value)}
              className="movie-input"
              placeholder="Enter a movie you like..."
            />
          </div>
          
          <button className="search-button" onClick={handleSearch}>
            <span>Get Recommendations</span>
            <i className="fas fa-arrow-right"></i>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Home;