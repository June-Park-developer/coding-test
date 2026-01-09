def solution(word):
    # 1. DFS 사용
    dictionary = []
    def dfs(current_word):
        if len(current_word) > 5:
            return
        if current_word != "":
            dictionary.append(current_word)
        for letter in ['A', 'E', 'I', 'O', 'U']:
            dfs(current_word+letter)
    dfs("")
    return dictionary.index(word) + 1
    
    # 2. product 라는 라이브러리 사용