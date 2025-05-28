/* 내 답안

const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

const N = Number(input[0]);
let count = 0;
for (let i = 1; i <= N;i++) {
    const word = input[i];
    const diff = [word[0]];
    for(let j = 1;j < word.length;j++){
        if(word[j-1] !== word[j]) {
            diff.push(word[j]);
        }}
    const set = new Set(diff);
    if(set.size === diff.length) {
        count ++;
    }
    }
console.log(count);

*/

// 모범답안

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input[0]);
let count = 0;

for (let i = 1; i <= N; i++) {
  const word = input[i];
  const seen = new Set();
  let isGroup = true;

  for (let j = 0; j < word.length; j++) {
    if (j > 0 && word[j] !== word[j - 1]) {
      if (seen.has(word[j])) {
        isGroup = false;
        break;
      }
    }
    seen.add(word[j]);
  }

  if (isGroup) count++;
}

console.log(count);
