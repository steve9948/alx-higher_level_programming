#!/usr/bin/node
console.log(factorial(parseInt(process.argv[2])));

function factorial (fact) {
  if (isNaN(fact)) {
    return 1;
  } else if (fact === 0) {
    return 1;
  } else {
    return fact * factorial(fact - 1);
  }
}
