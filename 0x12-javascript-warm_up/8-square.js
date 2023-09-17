#!/usr/bin/node

const arg2 = process.argv[2];
const size = parseInt(arg2);

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
