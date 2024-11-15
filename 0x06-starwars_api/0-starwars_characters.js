#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  
  const characters = data.characters;
  for (let i = 0; i < characters.length; i++) {
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
