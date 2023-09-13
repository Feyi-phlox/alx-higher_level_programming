#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
  if (err1) {
    process.exit(1);
  }

  fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
    if (err2) {
      process.exit(1);
    }

    const concatenatedData = data1 + data2;

    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err3) => {
      if (err3) {
        process.exit(1);
      }
    });
  });
});
