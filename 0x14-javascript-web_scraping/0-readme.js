#!/usr/bin/node

process.on('uncaughtException', error => console.log(error));
const fs = require('fs');
const file = fs.createReadStream(process.argv[2], 'utf8');
file.pipe(process.stdout);
