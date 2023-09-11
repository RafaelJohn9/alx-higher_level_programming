#!/usr/bin/node

/**
 * checks if an arg has been passed through
 */

const arg = process.argv;
if (arg.length === 2) {
  console.log('No argument');
} else if (arg.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
