#!/usr/bin/node
let argument = process.argv;
if (argument[2] === undefined || isNan(argument[2])) {
  console.log('Missing size');
} else {
  const x = Number(argument[2]);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
