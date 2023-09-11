#!/usr/bin/node

// a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const arg = process.argv;
const num = parseInt(arg[2]);

if (!isNaN(num)) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
