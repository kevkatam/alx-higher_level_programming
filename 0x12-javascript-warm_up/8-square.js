#!/usr/bin/node
const { argv } = require('process');
const number = parseInt(argv[2]);
if (Number.isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0, sqr; i < number; i++) {
    sqr = '';
    for (let j = 0; j < number; j++) {
      sqr += 'X';
    }
    console.log(sqr);
  }
}
