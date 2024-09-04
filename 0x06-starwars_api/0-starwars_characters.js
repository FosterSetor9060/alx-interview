#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];  // First positional argument is the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;  // SWAPI URL with movie ID

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;  // Array of character URLs

  characters.forEach((characterUrl) => {
    request(characterUrl, (err, res, charBody) => {
      if (err) {
        console.error('Error:', err);
        return;
      }
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);  // Print character name
    });
  });
});
