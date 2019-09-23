#!/usr/bin/node

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) { console.log(row); }
  }
};
