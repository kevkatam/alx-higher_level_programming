#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

request(argv[2], function (error, response, body) {
  if (error == null) {
    const res = {};
    const json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
	if (res[json[i].userId] === undefined) {
	  res[json[i].userId] = 0;
	}
	res[json[i].userId]++;
     }
    }
    console.log(res);
  }
});
