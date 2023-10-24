#!/usr/bin/node

/**
 * a script that writes  string to a file
 * first arg is the file path
 * second arg is the str to write
 * content must be written utf-8  encoding
 * if an error use object error code
 */

const fs = require('fs');

const filePath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filePath, data, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
