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