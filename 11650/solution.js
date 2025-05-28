/* 내 답안

const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().trim().split('\n');


const N = Number(input[0]);
const coordinateArray = []; // 좌표들의 2차원 배열

for (let i = 1; i <= N; i++){
    const str = input[i].trim().split(' ');
    const num = str.map((s) => +s);
    coordinateArray.push(num);
}

coordinateArray.sort((a, b) => {
    if((a[0] - b[0]) !== 0) {return (a[0]-b[0]);}
    else {return (a[1]-b[1]);}
} );

for (const i of coordinateArray) {
    console.log(i[0], i[1]);
}
*/

// 모범답안

const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .slice(1)
  .map((el) => el.split(" ").map(Number));

const solution = (input) => {
  return input
    .sort((a, b) => {
      return a[0] === b[0] ? a[1] - b[1] : a[0] - b[0];
    })
    .map((el) => el.join(" "))
    .join("\n");
};
