#!/usr/bin/node

const request = require('request');

// Movie ID is passed as the first argument
const movieId = process.argv[2];

// Construct the API URL for the specified movie
const url = `https://swapi.dev/api/films/${movieId}/`;

// Send a GET request to the API
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  // Parse the response body to JSON
  const data = JSON.parse(body);
  
  // Iterate over the characters array and print each character name
  const characters = data.characters;
  for (let i = 0; i < characters.length; i++) {
    // For each character, request their details
    request(characters[i], (err, res, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
