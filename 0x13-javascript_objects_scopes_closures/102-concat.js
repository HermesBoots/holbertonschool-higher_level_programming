#!/usr/bin/node

const fs = require('fs');

function copyFile (inFile, outFile) {
  let bytesRead = 1;
  const buffer = Buffer.alloc(8192);
  while (bytesRead > 0) {
    bytesRead = fs.readSync(inFile, buffer, 0, 8192, null);
    let writtenTotal = 0;
    let written = 1;
    while (written > 0 && writtenTotal < bytesRead) {
      written = fs.writeSync(
        outFile,
        buffer,
        writtenTotal,
        bytesRead - writtenTotal
      );
      writtenTotal += written;
    }
  }
}

let fileIn = fs.openSync(process.argv[2], 'r');
const fileOut = fs.openSync(process.argv[4], 'w');
copyFile(fileIn, fileOut);
fs.closeSync(fileIn);
fileIn = fs.openSync(process.argv[3], 'r');
copyFile(fileIn, fileOut);
fs.closeSync(fileIn);
fs.closeSync(fileOut);
