#!/usr/bin/node

exports.esrever = function (list) {
  const ret = Array(list.length);
  let left = 0;
  let right = list.length - 1;
  while (right >= 0) {
    ret[left] = list[right];
    left++;
    right--;
  }
  return ret;
};
