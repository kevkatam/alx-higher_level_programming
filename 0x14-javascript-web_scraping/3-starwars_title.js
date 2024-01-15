#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
request('https://swapi-api.alx-tools.com/api/films/' + argv[2] + '/', function (error, response, body) {
  if (error == null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
