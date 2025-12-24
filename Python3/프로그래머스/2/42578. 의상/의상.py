def solution(clothes):
    hash_map = {}
    for _, category in clothes:
        if category in hash_map:
            hash_map[category] += 1
        else:
            hash_map[category] = 1
    
    answer = 1
    for count in hash_map.values():
        answer *= (count + 1)
    return answer - 1