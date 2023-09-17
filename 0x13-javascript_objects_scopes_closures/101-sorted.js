#!/usr/bin/node
const dict = require('./101-data').dict;

const userDict = {};

for (const userID in dict) {
  const occurrences = dict[userID];

  if (!userDict[occurrences]) {
    userDict[occurrences] = [];
  }

  userDict[occurrences].push(userID);
}

console.log(userDict);
