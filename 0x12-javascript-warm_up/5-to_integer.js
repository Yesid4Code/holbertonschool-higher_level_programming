#!/usr/bin/nodejs
/**
 * Script that prints two arguemnts passed to it, using the next format.
 */
const number = parseInt(process.argv[2]);
if (number) {
  console.log('My number: ' + number)
} else {
  console.log('Not a number');
}
