def solution(s):
    nums = s.split(" ")
    numbers = list(map(lambda x: int(x), nums))
    min_num = min(numbers)
    max_num = max(numbers)
    return f"{min_num} {max_num}"

    
    
    