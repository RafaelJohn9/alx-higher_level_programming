#!/usr/bin/node

// a class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.print = function () {
        const line = 'X'.repeat(w);
        for (let i = 0; i < h; i++) {
          console.log(line);
        }
      };
    }
  }
}

module.exports = Rectangle;
