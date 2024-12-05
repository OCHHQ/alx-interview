#!/usr/bin/node

const request = require('request');

// Check if movie ID is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to get character name from URL
function getCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

// Main function to get and display characters
request(filmUrl, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const film = JSON.parse(body);
    const characters = film.characters;

    // Get all character names in order
    for (const characterUrl of characters) {
      try {
        const name = await getCharacterName(characterUrl);
        console.log(name);
      } catch (err) {
        console.error('Error fetching character:', err);
      }
    }
  } catch (parseError) {
    console.error('Error parsing response:', parseError);
  }
});
