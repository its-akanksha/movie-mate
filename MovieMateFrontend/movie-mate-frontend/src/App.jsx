import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import Recommendations from "./components/Recommendations";
import Navbar from "./components/Navbar";
import { MovieProvider } from "./context/MovieContext";
import "./App.css";

function App() {
  return (
    <MovieProvider>
      <Router>
        <div className="app-container">
          <Navbar />
          <div className="content-container">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/recommendations/:userId/:movieTitle" element={<Recommendations />} />
            </Routes>
          </div>
        </div>
      </Router>
    </MovieProvider>
  );
}

export default App;