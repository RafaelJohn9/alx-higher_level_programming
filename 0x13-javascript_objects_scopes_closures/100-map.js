#!/usr/bin/node

// a script that imports an array and computes a new array

const data = require('./100-data.js');
const originalList = data.list;

console.log(originalList);
const newList = originalList.map((x, idx) => x * idx);
console.log(newList);
