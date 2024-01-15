#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
request(argv[2], function (error, response) {
  if (error == null) {
    console.log('code: ' + response.statusCode);
  }
});
