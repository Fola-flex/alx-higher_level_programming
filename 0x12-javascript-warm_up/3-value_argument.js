#!/usr/bin/node

let arguments = process.argv;

function argumentValue (arguments) {
  if (arguments[2]) {
    return arguments[2]
  } else {
    return 'No argument'
  }
}

console.log(argumentValue(arguments))
