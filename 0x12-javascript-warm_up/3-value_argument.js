#!/usr/bin/node
const args = process.argv;
const len = args.length;
if (len <= 2) {
  console.log('No argument');
} else {
 console.log(process.argv[2]);
}
