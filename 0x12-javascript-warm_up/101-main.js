#!/usr/bin/node

// it is used as a test case for the function callMeMoby

const callMeMoby = require('./101-call_me_moby').callMeMoby;

callMeMoby(3, function () {
  console.log('C is fun');
});
