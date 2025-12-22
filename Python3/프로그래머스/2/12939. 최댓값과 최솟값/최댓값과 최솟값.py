def solution(s):
    nums = s.split(" ")
    numbers = list(map(lambda x: int(x), nums))
    min_num = min(numbers)
    max_num = max(numbers)
    return f"{min_num} {max_num}"

# 다른 사람 풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
    
# 가져갈 것
## map 은 list() 로 한번 감싸줘야 함
## min(이터러블), max(이터러블)  => 전반적으로 메서드가 어디껀지가 헷갈림;;
## str() 도 사용 가능
## f-string 사용법
