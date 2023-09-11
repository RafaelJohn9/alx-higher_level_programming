#!/usr/bin/node

// a script that prints x times "C is fun"

const listOfArgs = process.argv;
const arg = parseInt(listOfArgs[2], 10);
const sentence = 'C is fun';
let i = 0;

if (!isNaN(arg)) {
  while (i < arg) {
    console.log(sentence);
    i += 1;
  }
} else if (listOfArgs[2] === undefined) {
  console.log('Missing number of occurrences');
}
