#!/usr/bin/node
const argument = process.argv;
if (argument[2] === undefined || isNaN(argument[2])) {
  console.log('Missing size');
} else {
  const x = Number(argument[2]);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
