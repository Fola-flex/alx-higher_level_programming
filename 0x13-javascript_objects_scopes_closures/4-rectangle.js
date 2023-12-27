#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (( w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const newWidth = this.width;
    this.width = this.height;
    this.height = newWidth;
  }

  double () {
    this.width = w * 2;
    this.height = h * 2;
}

module.exports = Rectangle;
