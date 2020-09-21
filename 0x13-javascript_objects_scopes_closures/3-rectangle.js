#!/usr/bin/nodejs
/**
 * Class that define a rectangle and print a rectangle.
 */
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
  print () {
    let i;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
