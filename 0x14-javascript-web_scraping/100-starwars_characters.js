#!/usr/bin/node

/**
 * a script that prints all characters of star wars movie
 * the first arg is the movie id example 3 = return of the jedi
 * display one character name by line
 * you must use the starwars api
 * you must use the module request
 */

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    for (const character of data.characters) {
      request.get(character, (err, resp, info) => {
        if (err) {
          console.error(err);
        } else {
          const userData = JSON.parse(info);
          console.log(userData.name);
        }
      });
    }
  }
});
