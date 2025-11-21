def solution(nums):
    nums.sort()
    hash = []
    for num in nums:
        if len(hash) >= len(nums)//2:
            return len(hash)
        if num not in hash:
            hash.append(num)
    return len(hash)
    