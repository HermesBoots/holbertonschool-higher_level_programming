#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], { json: true }, function (error, response, body) {
  if (error) { return; }
  const ret = {};
  for (const task of body) {
    if (task.completed === true) {
      if (ret[task.userId] === undefined) { ret[task.userId] = 0; }
      ret[task.userId]++;
    }
  }
  console.log(ret);
});
