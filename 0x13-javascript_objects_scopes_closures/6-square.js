#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) { console.log(row); }
  }
};
