function solution(arr) {
  const answer = [];
  let pointer = -1;
  for (const number of arr) {
    if (pointer === -1) {
      answer.push(number);
      pointer++;
    }
    if (number !== answer[pointer]) {
      answer.push(number);
      pointer++;
    }
  }

  return answer;
}
