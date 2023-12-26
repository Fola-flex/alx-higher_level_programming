#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const lastValue = list[len];
    list[len] = lastValue;
    list[i] = lastValue;
    i++;
    len--;
  }
  return list;
};
