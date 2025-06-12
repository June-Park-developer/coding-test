function solution(progresses, speeds) {
  const N = progresses.length;
  const days = [];
  const answers = [];
  for (let i = 0; i < N; i++) {
    const day = Math.ceil((100 - progresses[i]) / speeds[i]);
    days.push(day);
  }
  console.log(days);
  let pointer = 1;
  while (days.length !== 0) {
    if (days[pointer] && days[0] >= days[pointer]) {
      pointer++;
    } else {
      answers.push(pointer);
      days.splice(0, pointer);
      pointer = 1;
    }
  }
  return answers;
}

// 1. 며칠 걸리는지 배열로 저장하자 => [7, 3, 9]
// 2. 첫번째부터 자기보다 작은 거 세면서 (count), 지워 (shift)
// 3. 매회 몇개 빠지는지 모르니까 while (배열 ! isEmpty) 로 반복하자
