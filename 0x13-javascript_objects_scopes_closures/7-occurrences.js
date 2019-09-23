#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let index = list.indexOf(searchElement);
  while (index >= 0) {
    index = list.indexOf(searchElement, index + 1);
    count++;
  }
  return count;
};
