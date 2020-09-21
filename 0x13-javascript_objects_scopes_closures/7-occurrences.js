#!/usr/bin/nodejs
/**
 * Function that returns the number of occurrences in a list.
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let item = '';
  for (item of list) {
    if (item === searchElement) {
      count++;
    }
  }
  return count;
};
