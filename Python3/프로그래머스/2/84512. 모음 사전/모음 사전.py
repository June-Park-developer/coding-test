def solution(word):
    dictionary = []
    def dfs(current_word):
        if len(current_word) > 5:
            return
        if current_word != "":
            dictionary.append(current_word)
        for letter in ['A', 'E', 'I', 'O', 'U']:
            dfs(current_word+letter)
    dfs("")
    dictionary.sort()
    return dictionary.index(word) + 1
            