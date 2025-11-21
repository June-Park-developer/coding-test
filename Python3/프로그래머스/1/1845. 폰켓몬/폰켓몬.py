// 처음 풀이
// 기존에 담기지 않은 것만 모아서 수를 세되
// 최대 개수를 넘기면 더 할 필요 없음

def solution(nums):
    nums.sort()
    hash = []
    for num in nums:
        if len(hash) >= len(nums)//2:
            return len(hash)
        if num not in hash:
            hash.append(num)
    return len(hash)

// set() 를 이용한 풀이

def solution(nums):
    return min(len(nums)//2, len(set(nums)))
