#!/usr/bin/nodejs
/**
 * Class that define a square and inherits from Rectangle of 4-rectangle.js
 */
class Square extends require('./5-square') {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    console.log(c.repeat(this.height));
  }
}

module.exports = Square;
