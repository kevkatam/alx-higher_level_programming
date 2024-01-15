#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
fs.readFile(argv[2], 'utf8', function (error, content) {
  if (content === undefined) {
    console.log(error);
  } else {
    console.log(content);
  }
});
