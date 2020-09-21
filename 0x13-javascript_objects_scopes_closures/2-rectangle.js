#!/usr/bin/nodejs
/**
 * Class that define a rectangle.
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    }
    return this
  }
}

module.exports = Rectangle;
