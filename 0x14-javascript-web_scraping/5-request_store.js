#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const file = fs.createWriteStream(process.argv[3], 'utf8');
request.get(process.argv[2]).pipe(file);
