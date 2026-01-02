def solution(citations):
    h = 0
    citations.sort(reverse=True)
    
    # for i in range(len(citations)):
    #     if (i+1) > citations[i]:
    #         return i
    # return len(citations)
    
# 코드를 효율적으로 짜보자. 경계를 잘 생각할 것
# enumerate 를 사용한 코드도 짜보자
    for i, cite in enumerate(citations, start=1):
        if i > cite:
            return i - 1
    return len(citations)