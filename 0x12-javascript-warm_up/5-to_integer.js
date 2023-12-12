#!/usr/bin/node

let argument = process.argv;

function toInteger(argument) {
	if (parseInt(argument[1]) {
		return "My number: " + parseInt(argument[1]) 
	} else {
		return "Not a number"
	}
}

console.log(toInteger(argument));
