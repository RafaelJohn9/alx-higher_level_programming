#!/usr/bin/node

// a function that prints the number of arguments already printed and the new arg val.

let index = 0;

function logMe (str) {
  console.log('%d: %s', index++, str);
}

module.exports = {
  logMe
};
