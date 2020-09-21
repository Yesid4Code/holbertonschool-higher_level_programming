#!/usr/bin/nodejs
/**
 * Class that define a square and inherits from Rectangle of 4-rectangle.js
 */
class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i;
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
