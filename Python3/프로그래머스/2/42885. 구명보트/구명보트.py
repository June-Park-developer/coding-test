def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    fattest = 0
    lightest = len(people)-1
    
    while fattest < lightest:
        if people[fattest] + people[lightest] <= limit:
            answer += 1
            fattest += 1
            lightest -= 1
        else:
            answer += 1
            fattest += 1
        
    if fattest == lightest:
        answer += 1
    
    return answer