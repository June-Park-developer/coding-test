def solution(s):
    pointer = -1
    stack = [0 for i in range(0, len(s))]
    for letter in s:
        if letter == '(':
            pointer += 1
            stack[pointer] = 1
        elif letter == ')':
            if stack[pointer]:
                stack[pointer] = 0
                pointer -= 1
                continue
            else: return False
    if sum(stack) != 0:
        return False
    return True