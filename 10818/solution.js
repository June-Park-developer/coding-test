// 내가 처음 한 풀이
/*
const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const firstLine = input[0];          // N
const secondLine = input[1];         // 1 2 3 4 5

const letters = secondLine.split(" ");
const numbers = letters.map((letter) => +letter);
const assorted = numbers.sort((a,b) => a-b);

const min = numbers[0];
const max = assorted[Number(firstLine) -1];

console.log(`${min} ${max}`);
*/

// 모범답안
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let b = input[1].split(" ");

console.log(Math.min(...b), Math.max(...b));
