#!/usr/bin/node
let argument = process.argv;
function add (a, b) {
  const c = a + b;
  console.log(c);
}

add(Number(argument[2]), Number(argument[3]));
