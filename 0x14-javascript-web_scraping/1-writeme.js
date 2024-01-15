#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
fs.writeFileSync(argv[2], argv[3]);
