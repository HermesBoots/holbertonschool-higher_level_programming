#!/usr/bin/node

const request = require('request');
request.get(
  process.argv[2],
  { json: true },
  function (error, response, body) {
    if (error) { return; }
    let count = 0;
    for (const film of body.results) {
      for (const person of film.characters) {
        if (person.indexOf('people/18') >= 0) { count++; }
      }
    }
    console.log(count);
  }
);
