#!/usr/bin/nodejs
/**
 * Scrip that search the second biggest integer in a list of arguments
 */
const args = process.argv;
const length = args.length;
if (length > 1) {
  args.sort();
  console.log(args[length - 1]);
} else {
  console.log('0');
}
