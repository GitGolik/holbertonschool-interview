#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi.dev/api/films/' + movieId + '/';

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  let completed = 0;

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (charErr, charResponse, charBody) {
      if (charErr) {
        console.error(charErr);
        return;
      }

      const character = JSON.parse(charBody);
      characters[i] = character.name;
      completed++;

      if (completed === characters.length) {
        for (let j = 0; j < characters.length; j++) {
          console.log(characters[j]);
        }
      }
    });
  }
});
