#!/usr/bin/node

const request = require('request');

request(`https://swapi.dev/api/films/${process.argv[2]}/`, (err, res, body) => {
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
