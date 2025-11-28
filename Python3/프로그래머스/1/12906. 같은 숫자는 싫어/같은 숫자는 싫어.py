def solution(arr):
    answer = []
    answer.append(arr[0])
    pointer = 0
    for i in range(1, len(arr)):
        if answer[pointer] != arr[i]:
            answer.append(arr[i])
            pointer += 1
    return answer