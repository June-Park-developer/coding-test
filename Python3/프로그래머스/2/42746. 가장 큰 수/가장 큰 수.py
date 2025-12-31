def solution(numbers):
    # 자리수는 정해지니까, 앞자리 수가 최대한 크도록 비교하는거네
    # 근데 3, 30, 34 를 비교할 때는 34 > 3 > 30 으로 되네 : 3 을 33으로 취급하는 건가
    
    strings = list(map(str, numbers))
    strings.sort(key = lambda x: x*3, reverse=True)
    answer = "".join(strings)
    
    return "0" if answer[0] == "0" else answer
        