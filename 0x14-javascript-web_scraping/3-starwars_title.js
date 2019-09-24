#!/usr/bin/node

const request = require('request');
request.get(
  'http://swapi.co/api/films/' + process.argv[2],
  { json: true },
  function (error, response, body) {
    if (error) { return; }
    console.log(body.title);
  }
);
