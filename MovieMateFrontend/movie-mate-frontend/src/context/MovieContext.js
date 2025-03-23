import React, { createContext, useState, useEffect } from "react";
import { getAllMovies } from "../services/recommenderService";

export const MovieContext = createContext();

export const MovieProvider = ({ children }) => {
    const [allMovies, setAllMovies] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchMovies = async () => {
            setLoading(true);
            try {
                const movies = await getAllMovies();
                setAllMovies(movies);
            } catch (error) {
                console.error("Error fetching movies:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchMovies();
    }, []);

    return (
        <MovieContext.Provider value={{ allMovies, loading }}>
            {children}
        </MovieContext.Provider>
    );
};