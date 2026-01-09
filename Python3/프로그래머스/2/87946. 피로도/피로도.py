from itertools import permutations
def solution(k, dungeons):
    # 1. 순열을 이용해서
    # counts = []
    # for p in permutations(dungeons, len(dungeons)):
    #     current = k
    #     count = 0
    #     for minimum, usage in p:
    #         if current >= minimum: 
    #             count += 1
    #             current -= usage
    #     counts.append(count)
    # return max(counts)

    # DFS 를 이용해서
    n = len(dungeons)
    visited = [False] * n
    
    max_count = 0
    def dfs(k, count):
        nonlocal max_count
        max_count = max(max_count, count)
        for i in range(n):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k-dungeons[i][1], count+1)
                visited[i] = False
    
    dfs(k, 0)
    return max_count

        