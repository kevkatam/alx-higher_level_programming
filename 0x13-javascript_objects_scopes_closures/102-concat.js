#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');

const first = fs.readFileSync(argv[2]).toString();
const second = fs.readFileSync(argv[3]).toString();
fs.writeFileSync(argv[4], first + second);
