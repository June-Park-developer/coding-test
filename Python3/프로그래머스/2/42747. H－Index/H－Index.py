def solution(citations):
    citations.sort(reverse = True)
    count = 0
    candidates = []
    h = citations[0]  
    for cite in citations:
        count += 1
        if count <= cite: candidates.append(count)
    if len(candidates) == 0 : return 0
    return candidates.pop()
# 코드를 효율적으로 짜보자. 경계를 잘 생각할 것
# enumerate 를 사용한 코드도 짜보자