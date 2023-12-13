#!/usr/bin/node
let argumnent = process.argv;
if (argument[2] === undefined || isNan(argument[2])) {
	console.log('Missing number of occurrences');
} else {
	const x = Number(argument[2]);
	let i = 0;
	while (i < x) {
		console.log('C is fun');
		i++;
	}
}
