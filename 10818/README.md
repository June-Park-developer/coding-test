## 새로 배운 개념

<aside>

## `Math.min`, `Math.max`

- **기능**
  - 숫자들의 최소, 최대

```tsx
Max.min(1, 2, 3, 4); // 숫자들 중 최솟값
Max.max(1, 2, 3, 4); // 숫자들 중 최댓값

// 배열이면 스프레드로 풀어서
const arr = [1, 2, 3, 4];
Math.min(...arr);
Math.max(...arr);
```

- **인수**
  - 숫자들을 인수로 받음
  - 배열로 받을 수는 없음 ⇒ 스프레드로 숫자로 풀어야 함
- **주의사항**
  - 배열이 비어있으면 Infinity, -Infinity 나오니까 체크할 것
- **시간복잡도** - **`sort`** : O(n logn) → 중간 애들도 다 정렬하게 됨 (Merge Sort의 일종) - **`Math.min/max`** : O(n) → 단순 비교만 n번
</aside>

<aside>

## 입력 처리 : `fs`

```tsx
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
```

- **결과**
  - 입력을 받아서 줄별로 문자열의 배열로 변경
- **설명**
  ```tsx
  fs.readFileSync("/dev/stdin"); // 여기까지는 Buffer 데이터
  ```
  - **`/dev/stdin`**
    - 표준 입력, 즉 사용자가 터미널에 입력하는 내용을 의미함.
  - **`readFileSync`**
    - 파일을 동기적으로 읽는 함수.
    - 사용자 입력이 들어올 때까지 기다림.
- **정리**
  | **부분** | **의미** |
  | --- | --- |
  | `fs.readFileSync("/dev/stdin")` | 표준 입력을 읽는다 (Buffer 형태) |
  | `.toString()` | 문자열로 변환 |
  | `.trim()` | 앞뒤 공백 제거 |
  | `.split("\n")` | 줄 단위로 배열로 나눔 |
  </aside>

---

## 추가로 주의할 점

- 문자열은 숫자로 바꾸는 과정 (`Number()`) 꼭 신경쓰기
- `sort` 는 원래 배열을 정렬하기 때문에 또 다른 변수에 안 받아도 됨
