#!/usr/bin/node

// a function that returns the number of occurrences in a list

function nbOccurences (list, searchElement) {
  let num = 0;
  for (const element of list) {
    if (element === searchElement) {
      num++;
    }
  }
  return (num);
}

module.exports = {
  nbOccurences
};
