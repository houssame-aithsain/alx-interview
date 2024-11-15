#!/usr/bin/node

const request = require('request');

const getCharacters = (urls, index) => {
  if (index === urls.length) return;
  request(urls[index], (err, response, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      getCharacters(urls, index + 1);
    }
  });
};

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (err, response, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    getCharacters(characters, 0);
  }
});
