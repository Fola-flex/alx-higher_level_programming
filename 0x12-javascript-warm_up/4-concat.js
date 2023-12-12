#!/usr/bin/node

let arguments = process.argv;
let new_arguments = arguments.splice(0, 1);
let concat_arguments = new_arguments.join(" is ");

console.log(concat_arguments);
