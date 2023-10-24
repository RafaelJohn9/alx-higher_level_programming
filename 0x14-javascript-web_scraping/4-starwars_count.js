#!/usr/bin/node

/**
 * a script that prints the number of movies where the char
 * "Wedge antillies" is present
 * first arg is the url to the star wars api
 * wedge anillies character id is 18
 * script must use the char id to filter the result
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
