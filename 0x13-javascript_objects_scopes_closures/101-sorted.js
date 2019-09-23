#!/usr/bin/node

const dict = require('./101-data.js').dict;
const ret = {};
for (const key in dict) {
  if (ret[dict[key]] === undefined) { ret[dict[key]] = []; }
  ret[dict[key]].push(key);
}
console.log(ret);
