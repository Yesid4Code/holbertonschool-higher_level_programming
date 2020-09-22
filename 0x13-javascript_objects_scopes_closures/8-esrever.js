#!/usr/bin/nodejs
/**
 * Function that returns the number of occurrences in a list.
 */
exports.esrever = function (list) {
  let l = list.length;
  let tmp = '';
  for (let i = 0; i < l; i++, l--) {
    tmp = list[i];
    list[i] = list[l - 1];
    list[l - 1] = tmp;
  }
  return list;
};
