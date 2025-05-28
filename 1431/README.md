## 배운 것

- 입력도 더 빠르게 한번에 받아버릴 수 있구나..!
- 함수로 뺀 것이 역시 좋군
- sort 할 때 || 를 통해서 0 이면 자동으로 다음 꺼로 넘어가게 했구나..!
- 숫자인지 볼 때 `.match` 와 정규식을 이용했음

<aside>

### `.reduce`

- **기능**
  - 배열을 순회하면서 누적 값을 만든다.
- **형태**
      ```jsx
      array.reduce((accumulator, currentValue) => {
        return updatedAccumulator;
      }, initialValue);
      ```

      - accumulator: 누적된 결과값
      - currentValue: 현재 순회 중인 값
      - initialValue: 누산기의 초기값
  </aside>

<aside>

### `.match`

- **기능**
  - 문자열에서 특정 패턴(정규표현식)에 맞는 값을 찾아서 배열로 반환
- **형태**
  ```jsx
  string.match(정규표현식);
  ```
  - 문자열: 검색 대상
  - 정규표현식: 찾고 싶은 문자 패턴
- **주의할 점** - `g` 플래그가 없으면?
          ```jsx
          "abc123".match(/\d/);
          // 결과: ['1'] → 첫 번째만 반환
          ```

          - `g` 플래그 없으면 첫 번째 일치만 반환함
          - 여러 개 찾으려면 반드시 `/.../g`처럼 **g(global)** 플래그를 써야 함
      - 맞는 걸 못 찾으면?

          ```jsx
          "abc".match(/\d/g); // 숫자가 없음
          // 결과: null
          ```

          - 그래서 아까 코드에서 `numbers?.reduce(...) || 0` 이렇게 `null` 방어 코드가 들어간 거
  </aside>

<aside>

## `localeCompare()`

- **기능**
  - 앞의 문자열이 뒤의 문자열보다 사전적으로 앞인지, 뒤인지, 같은지를 숫자로 반환함
    | 반환값 | 의미                  |
    | ------ | --------------------- |
    | 음수   | `문자열1 < 문자열2`   |
    | 0      | `문자열1 === 문자열2` |
    | 양수   | `문자열1 > 문자열2`   |
  - `sort` 랑 같이 쓰기 완벽
- **형태**
  ```jsx
  str1.localeCompare(str2);
  ```

</aside>
