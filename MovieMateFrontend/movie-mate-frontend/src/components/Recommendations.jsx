import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { getRecommendations } from "../services/recommenderService";
import "./Recommendations.css";

const Recommendations = () => {
  const { userId, movieTitle } = useParams();
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRecommendations = async () => {
      setLoading(true);
      try {
        const movies = await getRecommendations(userId, decodeURIComponent(movieTitle));
        setRecommendations(movies);
      } catch (error) {
        console.error("Error fetching recommendations:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchRecommendations();
  }, [userId, movieTitle]);

  return (
    <div className="recommendations-container">
      <h1>Recommended Movies</h1>
      <div className="movie-query-info">
        <p>
          Based on <span className="highlight">{decodeURIComponent(movieTitle)}</span> for User ID: {userId}
        </p>
      </div>

      {loading ? (
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>Finding perfect matches for you...</p>
        </div>
      ) : (
        <div className="recommendations-grid">
          {recommendations.length > 0 ? (
            recommendations.map((movie, index) => (
              <div 
                key={index} 
                className="movie-card"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <div className="movie-poster">
                  <i className="fas fa-film poster-icon"></i>
                </div>
                <div className="movie-details">
                  <h3>{movie}</h3>
                  <div className="movie-rating">
                    {Array(5).fill().map((_, i) => (
                      <i key={i} className={`fas fa-star ${i < Math.floor(Math.random() * 2) + 3 ? 'filled' : ''}`}></i>
                    ))}
                  </div>
                </div>
              </div>
            ))
          ) : (
            <div className="no-results">
              <i className="fas fa-search"></i>
              <p>No recommendations found. Try a different movie.</p>
            </div>
          )}
        </div>
      )}
      
      <Link to="/" className="back-button">
        <i className="fas fa-arrow-left"></i> Back to Search
      </Link>
    </div>
  );
};

export default Recommendations;