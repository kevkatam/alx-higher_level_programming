#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
let noFilms = 0;
request(argv[2], function (error, response, body) {
  if (error == null) {
    const json = JSON.parse(body);
    const res = json.results;
    for (let i = 0; i < res.length; i++) {
      const chars = res[i].characters;
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].search('18') > 0) {
          noFilms++;
        }
      }
    }
  }
  console.log(noFilms);
});
