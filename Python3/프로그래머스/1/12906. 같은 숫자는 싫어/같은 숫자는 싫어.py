def solution(arr):
    answer = []
    answer.append(arr[0])
    pointer = 0
    for i in range(1, len(arr)):
        if answer[pointer] != arr[i]:
            answer.append(arr[i])
            pointer += 1
    return answer


# 슬라이싱을 사용할 수도 있음
def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer

## 포인트 a[-1:]
### 단순히 a[-1] 을 사용하면 마지막의 원소를 가져오고, 빈배열이면 오류 남
### 하지만 a[-1:] 을 사용하면 리스트의 슬라이싱이라 결과가 리스트고, 빈배열이면 그냥 빈배열이니까 괜찮
