#!/usr/bin/node

/**
 * Prints the first arg passed
 */

const arg = process.argv;
if (arg[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
