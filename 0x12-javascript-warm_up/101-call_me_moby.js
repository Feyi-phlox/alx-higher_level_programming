#!/usr/bin/node

// Define a function named "executeXTimes"
function executeXTimes(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
module.exports = { executeXTimes };
