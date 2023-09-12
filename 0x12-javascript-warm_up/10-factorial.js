#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg2 = process.argv[2];
const n = parseInt(arg2);

const result = factorial(n);
console.log(result);
