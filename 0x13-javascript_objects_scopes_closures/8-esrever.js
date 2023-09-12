#!/usr/bin/node

// a function that returns the reversed version of a list

function esrever (list) {
  const length = (list.length - 1);
  const newList = [];
  for (let i = length; i >= 0; i--) {
    newList.push(list[i]);
  }
  return (newList);
}

module.exports = {
  esrever
};
