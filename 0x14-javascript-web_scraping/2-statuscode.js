#!/usr/bin/node

/**
 * a script that display the status code of a GET request
 * the status code must be printed like this code: <status  code>
 * you must use the module request
 */

const request = require('request');

const url = process.argv[2];

request.get(url, (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', data.statusCode);
  }
});
