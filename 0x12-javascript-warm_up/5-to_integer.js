#!/usr/bin/node
const argument = process.argv;
function toInteger (argument) {
  if (parseInt(argument[2])) {
    return 'My number: ' + parseInt(argument[2]);
  } else {
    return 'Not a number';
  }
}
console.log(toInteger(argument));
