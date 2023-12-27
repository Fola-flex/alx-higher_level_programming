#!/usr/bin/node

const oldSquare = require('./5-square.js');

class Square extends oldSquare {
  constructor (size) {
    super (size)
  }
  
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'c';
      }
      console.log(s);
    }
  }
}