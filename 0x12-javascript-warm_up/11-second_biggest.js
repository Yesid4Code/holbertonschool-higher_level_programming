#!/usr/bin/nodejs
/**
 * Scrip that search the second biggest integer in a list of arguments
 */
const args = process.argv;
const length = args.length;
if (length > 3) {
  args.sort();
  console.log(args[length - 2]);
} else {
  console.log(0);
}
