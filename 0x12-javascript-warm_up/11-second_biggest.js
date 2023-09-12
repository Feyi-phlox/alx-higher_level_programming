#!/usr/bin/node

// Get the command-line arguments
const args = process.argv.slice(2);

// Convert the arguments to integers and filter out non-integer values
const integers = args.map(function (arg) {
  return parseInt(arg);
}).filter(Number.isInteger);

// Sort the integers in descending order
integers.sort((a, b) => b - a);

// If there are no valid integers or only one, print 0
if (integers.length <= 1) {
  console.log(0);
} else {
  // The second biggest integer will be at index 1 after sorting
  console.log(integers[1]);
}
