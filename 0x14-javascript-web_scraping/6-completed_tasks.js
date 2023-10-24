#!/usr/bin/node

/**
 * a script that computes the number of tasks completed by user id
 * the first arg is the api url
 * only prints the users with completed task
 * you must use the module request
 */

const request = require('request');
const url = process.argv[2];

const myDict = {};
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    for (const element of data) {
      if (element.completed === true) {
        if (myDict[element.userId]) {
          myDict[element.userId] += 1;
        } else {
          myDict[element.userId] = 1;
        }
      }
    }
    console.log(myDict);
  }
});
