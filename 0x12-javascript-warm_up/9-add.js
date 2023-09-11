#!/usr/bin/node

/**
 * add- a script that prints the addition of 2 int
 * @a: the first arg to be passed
 * @b: the seconf arg to be passed
 */

const listOfArgs = process.argv;
const firstNumber = parseInt(listOfArgs[2], 10);
const secondNumber = parseInt(listOfArgs[3], 10);

function add (a, b) {
  return (a + b);
}
if (isNaN(firstNumber) || isNaN(secondNumber)) {
  console.log(NaN);
} else {
  console.log(add(firstNumber, secondNumber));
}
