#!/usr/bin/node

// a script that imports an array and computes a new array

const list = require('./100-data.js').list;

console.log(list);
const newList = list.map(val => val * list.indexOf(val));
console.log(newList);
