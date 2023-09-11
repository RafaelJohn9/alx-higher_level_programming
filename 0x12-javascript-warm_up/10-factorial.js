#!/usr/bin/node

/**
 * Factorial: a script that computes and prints a factorial
 * @n: factorial number to reach
 * @Return: the answer
 */

const listOfArgs = process.argv;
const arg = parseInt(listOfArgs[2], 10);

function factorial (n) {
  let result = 1;
  if (n === 1) {
    return (1);
  } else {
    result *= factorial(n - 1);
    result *= n;
    return (result);
  }
}

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(factorial(arg));
}
