#!/usr/bin/node

let size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  size = Math.floor(size);
  for (let y = 0; y < size; y++) {
    console.log('X'.repeat(size));
  }
}
