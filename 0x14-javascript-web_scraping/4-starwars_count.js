#!/usr/bin/node

/**
 * a script that prints the title of Star Wars movie
 * where the episode number mathches a given integer
 * first arg is the movie id
 * you must use the starwars api
 * https://swapi-api.alx-tools.com/api/films/:id
 * you must use the module request
 */

const request = require('request');
const givenUrl = process.argv[2];
const url = `${givenUrl}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const count = body.split('people/18').length - 1;
    console.log(count);
  }
});
