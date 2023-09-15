#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
// First methode using Number function
// console.log(add(Number(process.argv[2]), Number(process.argv[3])));

// Second methode
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}