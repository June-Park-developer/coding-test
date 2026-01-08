def solution(n, computers):
    # DFS (재귀)
#     def dfs(v): 
#         visited[v] = True
        
#         for i in range(n):
#             if not visited[i] and computers[v][i]:
#                 dfs(i)
                
#     visited = [False] * n
#     count = 0
#     for i in range(n):
#         if not visited[i]:
#             count +=1
#             dfs(i)
        
        
#     return count
    
    
    # DFS (스택)
    def dfs(v):
        stack = [v]
        
        while stack:
            current = stack.pop()
            visited[current] = True
            for i in range(n):
                if not visited[i] and computers[current][i]:
                    stack.append(i)
    
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    return count