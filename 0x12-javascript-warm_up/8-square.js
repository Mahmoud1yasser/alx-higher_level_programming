#!/usr/bin/node
const firstArgumentAsInt = parseInt(process.argv[2], 10);
if (!isNaN(firstArgumentAsInt)) {
  let i;
  const str = 'X';
  for (i = 1; i < firstArgumentAsInt + 1; i++) {
    console.log(str.repeat(firstArgumentAsInt));
  }
} else {
  console.log('Missing size');
}
