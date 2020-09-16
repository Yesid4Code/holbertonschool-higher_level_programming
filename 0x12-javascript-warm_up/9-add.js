#!/usr/bin/nodejs
/**
 * Scrip that prints a square
 */
const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);

if (n1 && n2) {
    console.log(n1 + n2);
} else {
  console.log(NaN);
}
