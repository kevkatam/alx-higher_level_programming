#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const len = list.length - 1;
  let j = 0;
  for (let i = len; i >= 0; i--) {
    newList[j] = list[i];
    j++;
  }
  return (newList);
};
