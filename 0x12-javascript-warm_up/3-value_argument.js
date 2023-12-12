#!/usr/bin/node

let arguments = process.argv;

function argumentValue(arguments) {
	if (arguments[1]) {
		return arguments[1]
	} else {
		return "No argument"
	}
}

console.log(argumentValue(arguments))
