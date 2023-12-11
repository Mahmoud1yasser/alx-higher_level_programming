#!/usr/bin/node
const firstArgumentAsInt = parseInt(process.argv[2], 10);
if (!isNaN(firstArgumentAsInt)) {
  let i;
  for (i = 1; i < firstArgumentAsInt + 1; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
