#!/usr/bin/nodejs
/**
 * Scrip that compute the factorial of a number
 */
function facto (n) {
  if (n) {
    return (n * (facto(n - 1)));
  } else {
    return (1);
  }
}

console.log(facto(parseInt(process.argv[2])));
