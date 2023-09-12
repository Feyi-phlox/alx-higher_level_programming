#!/usr/bin/node
const arg2 = process.argv[2];
const arg3 = process.argv[3];

if (arg2 === undefined && arg3 === undefined) {
  console.log('undefined is undefined');
} else if (arg3 === undefined) {
  console.log(`${arg2} is undefined`);
} else {
  console.log(`${arg2} is ${arg3}`);
}
