#!/usr/bin/nodejs
/**
 * Scrip that prints a square
 */
function facto(n) {
  if (n) {
    return (n * (facto(n - 1)))
  } else {
    return (1);
  }
}

console.log(facto(parseInt(process.argv[2])));
