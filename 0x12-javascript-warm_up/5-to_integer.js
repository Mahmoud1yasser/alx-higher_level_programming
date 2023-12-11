#!/usr/bin/node
const firstArgumentAsInt = parseInt(process.argv[2], 10);
if (!isNaN(firstArgumentAsInt)) {
    console.log('My number:', firstArgumentAsInt);
  } else {
    console.log('Not a number');
  }
