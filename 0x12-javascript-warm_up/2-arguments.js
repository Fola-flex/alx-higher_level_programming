#!/usr/bin/node
let arguments = process.argv;

function printArgument(arguments) {
	if (arguments.length === 2) {
		return "No Argument"
	} else if (arg.length === 3) {
		return "Argument found"
	} else {
		return "Arguments found"
	}
}

console.log(printArgument(arguments));
