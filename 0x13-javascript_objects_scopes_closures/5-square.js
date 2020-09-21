#!/usr/bin/nodejs
/**
 * Class that define a square and inherits from Rectangle of 4-rectangle.js
 */
class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size)
  }
}
