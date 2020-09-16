#!/usr/bin/nodejs
/**
 * Scrip that prints a square
 */
const arg = parseInt(process.argv[2]);
if (arg) {
  for (const i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
} else {
  console.log('Missing size');
}
