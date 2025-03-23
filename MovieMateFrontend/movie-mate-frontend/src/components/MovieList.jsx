import React from "react";
import "./MovieList.css";

const MovieList = ({ movies, loading, onSelectMovie }) => {
  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading movies...</p>
      </div>
    );
  }

  return (
    <div className="movie-list">
      {movies.map((movie, index) => (
        <div 
          key={index} 
          className="movie-item"
          onClick={() => onSelectMovie(movie)}
        >
          {movie}
        </div>
      ))}
    </div>
  );
};

export default MovieList;