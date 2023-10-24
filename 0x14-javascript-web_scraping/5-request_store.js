#!/usr/bin/node

/**
 * a script that gets content of a web page
 * and stores it in a file
 * the first arg is the url to request
 * the second arg the file path to store the body response
 * the file must be utf-8 encodedd
 * you must use the module request
 */

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filepath, body, 'utf-8', (error, response) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
