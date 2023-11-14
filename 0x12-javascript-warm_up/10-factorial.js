#!/usr/bin/node
const { argv } = require('process');
function factorial (a) {
  a = parseInt(a);
  if (a === 1 || Number.isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(argv[2]));
