/* 내 답안

const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);

const total = new Array(N+1).fill(0);

for (let i = 1; i <= N; i++) {
    let score = 0;
    for (const result of input[i]) {
        if (result === 'X') {
            score = 0;
            continue;
        } 
        score ++;
        total[i] += score;
    }
}

for (let i = 1; i <= N; i++) {
    console.log(total[i]);
}
    */

// 모범답안

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input[0]);

for (let i = 1; i <= N; i++) {
  const line = input[i];
  let score = 0;
  let total = 0;

  for (const char of line) {
    if (char === "O") {
      score++;
      total += score;
    } else {
      score = 0;
    }
  }

  console.log(total);
}
