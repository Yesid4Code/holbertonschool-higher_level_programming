#!/usr/bin/nodejs
/**
 * Function that converts a number from base 1o to another.
 * The base is passed as argument:
 */
exports.converter = function (base) {
  function convert (number) {
    return (number.toString(base));
  }
  return convert;
};
