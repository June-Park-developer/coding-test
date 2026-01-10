from itertools import product
def solution(word):
    # 1. DFS 사용
#     dictionary = []
#     def dfs(current):
#         dictionary.append(current)
#         if len(current) == 5: return
#         for l in ['A', 'E', 'I', 'O', 'U']:
#             dfs(current + l)
    
#     dfs("")
#     return dictionary.index(word)
    
    # 2. product 라는 라이브러리 사용
    dictionary = []
    vowels = ['A','E','I','O','U']
    for i in range(1, 6):
        for p in product(vowels, repeat=i): # p 는 튜플임
                dictionary.append("".join(p))
    dictionary.sort()
    return dictionary.index(word) +1
    