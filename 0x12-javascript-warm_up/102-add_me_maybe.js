#!/usr/bin/node

// a function that incremets and calls a function

function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
}

module.exports = {
  addMeMaybe
};
