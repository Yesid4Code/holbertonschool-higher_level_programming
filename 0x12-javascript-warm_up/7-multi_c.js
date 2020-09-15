#!/usr/bin/nodejs
/* Script that prints 3 lines using an array of strings */
const x = parseInt(process.argv[2]);
let i = 0;
if (x) {
  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log("Missing number of occurrences");
}
