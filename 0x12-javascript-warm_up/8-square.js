#!/usr/bin/node

// a script that prints a square

const listOfArgs = process.argv;
const arg = listOfArgs[2];

if (!isNaN(arg)) {
  if (arg >= 0) {
    let i = 0;
    const width = 'X'.repeat(arg);
    while (i < arg) {
      console.log(width);
      i += 1;
    }
  }
} else {
  console.log('Missing size');
}
