#!/usr/bin/node

const arg2 = process.argv[2];
const arg3 = process.argv[3];
const int1 = parseInt(arg2);
const int2 = parseInt(arg3);

function add (a, b) {
  return a + b;
}
const result = add(int1, int2);
console.log(result);
