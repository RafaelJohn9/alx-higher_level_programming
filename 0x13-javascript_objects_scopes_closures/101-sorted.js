#!/usr/bin/node

// a script that imports a dictionary of occurrences by user id

const data = require('./101-data');

const originalDict = data.dict;
const sortedDict = {};

for (const userId in originalDict) {
  const occurrence = originalDict[userId];

  if (!sortedDict[occurrence]) {
    sortedDict[occurrence] = [];
  }

  sortedDict[occurrence].push(userId);
}

console.log(sortedDict);
