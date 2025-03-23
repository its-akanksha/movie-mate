# MovieMate - Movie Recommendation System

A modern web application that provides personalized movie recommendations using content-based and collaborative filtering techniques.

## Features

- Modern, responsive UI with animations and transitions
- Movie browsing through a collapsible side panel
- Personalized movie recommendations based on user ID and movie preferences
- Sleek dark theme with glass-morphism design elements
- Loading states and animations for a polished user experience

## Project Structure

The project follows a component-based architecture using React:

- `App.js`: Main component handling routing
- `MovieContext.js`: Context provider for managing movie data
- `Home.jsx`: Main search page with collapsible movie list panel
- `MovieList.jsx`: Scrollable list of available movies
- `Recommendations.jsx`: Grid display of recommended movies
- `recommenderService.js`: API service for fetching recommendations

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```
   npm install
   ```
3. Start the development server:
   ```
   npm start
   ```

## Integrating with Your Backend

Replace the mock implementations in `src/services/recommenderService.js` with your actual API calls to connect with your recommendation engine backend.

## Dependencies

- React 18
- React Router 6
- Font Awesome (for icons)
- Google Fonts (Poppins)

## Acknowledgments

- [Your acknowledgments here]