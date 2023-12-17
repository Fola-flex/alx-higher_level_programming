#!/usr/bin/node
const argument = process.argv;
if (argument.length === 2) {
  console.log('No Argument');
} else if (argument.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
