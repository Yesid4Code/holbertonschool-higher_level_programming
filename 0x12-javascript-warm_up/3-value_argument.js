#!/usr/bin/nodejs
/**
 * Script that prints the first arguemtn passed.
 */
"use strict";
if (process.argv.length > 1) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
