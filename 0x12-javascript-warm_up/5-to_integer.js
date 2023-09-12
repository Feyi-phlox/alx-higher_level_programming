#!/usr/bin/node
const arg2 = process.argv[2];
const number = parseInt(arg2);
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
