#!/usr/bin/node
const argument = process.argv;
function argumentValue (argument) {
  if (argument[2]) {
    return argument[2];
  } else {
    return 'No argument';
  }
}
console.log(argumentValue(argument))
