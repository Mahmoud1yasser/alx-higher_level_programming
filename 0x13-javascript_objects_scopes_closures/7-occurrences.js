#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0, i;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    } else {
      continue;
    }
  }
}
