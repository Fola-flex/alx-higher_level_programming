#!/usr/bin/node
const argument = process.argv;
if (argument.length <= 3) {
  console.log('0');
} else {
  const arr = argument.slice(2).map(Number);
  const second = arr.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
