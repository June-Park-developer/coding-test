def solution(s):
    chars = s.split(" ")
    numbers = list(map(lambda x:int(x), chars))
    min_number = min(numbers)
    max_number = max(numbers)
    return f"{min_number} {max_number}"
    
    
    