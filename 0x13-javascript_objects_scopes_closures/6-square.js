#!/usr/bin/node

// a class Square that defines a square and inherits from Square of 5-square.js

class Square extends require('./5-square.js') {
  charPrint (c = 'X') {
    const line = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
}

module.exports = Square;
