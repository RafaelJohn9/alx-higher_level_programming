#!/usr/bin/node

// a function that executes x times a function

function callMeMoby (num, func) {
  for (let i = 0; i < num; i++) {
    func();
  }
}

module.exports = {
  callMeMoby
};
