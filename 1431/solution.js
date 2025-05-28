/* 내 답안

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
const N = Number(input.shift()); // 이제 input에는 시리얼 번호만 0번째 부터 N-1 번째까지 있음

input.sort((a, b) => {
    if(a.length !== b.length) {
        return (a.length - b.length);
    }
    else
        {
            let numSumOfA = 0;
            let numSumOfB = 0;
            for (const letter of a) {
                if ('0' <= letter && letter <='9') {
                    numSumOfA += +letter;
                }
            }
            for (const letter of b) {
                if ('0' <= letter && letter <='9') {
                    numSumOfB += +letter;
                }
            }
            if (numSumOfA - numSumOfB !== 0){
                return numSumOfA - numSumOfB
            }
            else {
                
                    if(a<b) return -1;
                    if(a>b) return +1;
                
            }
        }
});

console.log(input.join("\n"));
*/

// 모범답안
const [N, ...input] = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

function sumOfNumbers(input) {
  const numbers = input.match(/\d/g);
  const sum = numbers?.reduce((acc, num) => acc + parseInt(num, 10), 0) || 0;
  return sum;
}

const sortedInput = input.sort(
  (a, b) =>
    a.length - b.length ||
    sumOfNumbers(a) - sumOfNumbers(b) ||
    a.localeCompare(b)
);

console.log(sortedInput.join("\n"));
