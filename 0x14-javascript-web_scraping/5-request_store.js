#!/usr/bin/node
/**
 * Script that gets the contents of a webpage
 * and stores it in a file.
 */
const fs = require('fs');
const request = require('request');
let url = process.argv[2];
request(url, 'utf-8').pipe(fs.createWriteStream(process.argv[3]));
