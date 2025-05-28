## 배운 점

<aside>

## 판단 및 break 타이밍

- 조건 판별은 가능한 한 빠르게 수행하고,
  불필요한 반복은 즉시 중단하는 것이 성능상 유리함
- `false`, `예외`, `불일치` 등의 결정적 조건이 발생하는 지점을
  명확히 인지하고 그 지점에서 바로 `break` 또는 `return` 하도록 하자!

> **판단은 빠르게, 중단은 과감하게**

</aside>

<aside>

## `Set`

- **기능**
  - 중복을 허용하지 않는 객체형 컬렉션
  - 순서가 있으나 인덱스로 접근하지는 않음 (Array 아님!)
- **배열 → Set**
  - `new Set(배열)`
- **Set → 배열**
  - `[...set]`
- **배열과 메서드 비교**
      | **기능** | **Set** | **Array**  | **설명** |
      | --- | --- | --- | --- |
      | 추가 | `set.add(value)` | `arr.push(value)` | 중복 시 Set은 무시함 |
      | 삭제 | `set.delete(value)` | `arr.splice(index, 1)` | Set은 값으로 삭제, Array는 index로 삭제 |
      | 포함 여부 | `set.has(value)` | `arr.includes(value)` | 포함 여부 빠르게 확인 |
      | 전체 삭제 | `set.clear()` | `arr = []` or `arr.length = 0` | 모두 제거 |
      | 크기 확인 | `set.size` | `arr.length` |  |
      | 순회 | `for (let x of set)` | `for (let x of arr)` | 가능함, 동일 문법 |
  </aside>
