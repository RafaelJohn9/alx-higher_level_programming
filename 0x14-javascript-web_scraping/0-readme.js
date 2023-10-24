#!/usr/bin/node

/**
 * a script that prints the content of a file
 * gives the object error if the file passed does not exist
 */

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
