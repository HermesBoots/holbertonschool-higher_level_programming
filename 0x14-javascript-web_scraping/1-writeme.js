#!/usr/bin/node

process.on('uncaughtException', error => console.log(error));
const fs = require('fs');
fs.writeFileSync(process.argv[2], process.argv[3], 'utf8');
