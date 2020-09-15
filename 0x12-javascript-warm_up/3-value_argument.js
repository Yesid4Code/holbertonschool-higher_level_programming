#!/usr/bin/nodejs
/**
 * Script that prints the first arguemnt passed.
 */
const arg = process.argv[2]
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
