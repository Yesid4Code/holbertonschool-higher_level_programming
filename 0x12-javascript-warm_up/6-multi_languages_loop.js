#!/usr/bin/nodejs
/* Script that prints 3 lines using an array of strings */
const array = ['C is fun', 'Python is cool', 'Javascript is amazing'];
let idx;
for (idx of  array) {
  console.log(array[idx]);
}
