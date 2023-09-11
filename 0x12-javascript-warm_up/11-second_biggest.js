#!/usr/bin/node

// a script that searches the second biggest integer in the list of arguments

const listOfArgs = process.argv.slice(2);

function findSecondMax (list) {
  let max = -Infinity;
  let secondMax = -Infinity;

  for (let num of list) {
    num = parseInt(num, 10);
    if (num > max) {
      secondMax = max;
      max = num;
    }
    else if (num > secondMax && num < max)
	  {
		  secondMax = num;
	  }
  }
  return (secondMax);
}

if (listOfArgs.length === 0 || listOfArgs.length === 1) {
  console.log(0);
} else {
  console.log(findSecondMax(listOfArgs));
}
