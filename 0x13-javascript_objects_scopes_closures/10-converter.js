#!/usr/bin/node

// a function that converts a num from base 10 to another base passed as arg

function converter (numToBeConverted) {
  function aConverter (n) {
    return (n.toString(numToBeConverted));
  }
  return (aConverter);
}

module.exports = {
  converter
};
