#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!(w > 0 && h > 0)) { return; }
    this.width = w;
    this.height = h;
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) { console.log(row); }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  print () {
    this.charPrint('X');
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
