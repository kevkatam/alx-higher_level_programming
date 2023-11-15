#!/usr/bin/node
const { argv } = require('process');
let temp = 0;
const array = [];
let j;

for (let i = 2; i < argv.length; i++) {
  if (!(Number.isNaN(argv[i]))) {
    array[i - 2] = parseInt(argv[i]);
  }
}

if (array.length > 1) {
  temp = Math.max.apply(null, array);
  j = array.indexOf(temp);
  array[j] = -Infinity;
  temp = Math.max.apply(null, array);
}
console.log(temp);
