#!/usr/bin/nodejs
/**
 * Class that define a rectangle.
 */
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
