#!/usr/bin/node
const Square1 = require('./5-square.js');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0, sqr; i < this.height; i++) {
      sqr = '';
      for (let j = 0; j < this.width; j++) {
        sqr += c;
      }
      console.log(sqr);
    }
  }
}
module.exports = Square;
