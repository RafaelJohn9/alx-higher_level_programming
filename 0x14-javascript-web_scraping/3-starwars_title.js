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
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
let episodeDict = {};

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    episodeDict = JSON.parse(body);
    console.log(episodeDict.title);
  }
});
