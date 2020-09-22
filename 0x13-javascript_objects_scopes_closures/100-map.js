#!/usr/bin/node
/* script that imports an array and computes a new array. */
const list = require('./100-data.js').list;
console.log(list); 
const newList = list.map((item, i) => item * i);
console.log(newList);
