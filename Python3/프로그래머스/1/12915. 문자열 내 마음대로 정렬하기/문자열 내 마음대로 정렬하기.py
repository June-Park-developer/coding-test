def solution(strings, n):
    # n 번째 글자들이 뭔지 일단 확인해야 하고
    # 그걸 sort 한 다음에..? 
    # 그게 원래 무슨 단어였는지를 인덱스를 기억해야하는건가? 
    # 정렬을 구현해야할 것 같은데 전혀 모르겠음 ~~
    return sorted(strings, key=lambda x: (x[n], x))