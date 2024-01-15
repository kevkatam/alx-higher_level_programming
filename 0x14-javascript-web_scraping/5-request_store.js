#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const fs = require('fs');
request(argv[2], function (error, response, body) {
  if (error == null) { fs.writeFileSync(argv[3], body); }
});
