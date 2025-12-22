def solution(s):
    words = s.split(" ")
    result = []
    for word in words:
        if word:
            new_word = word[0].upper() + word[1:].lower()
            result.append(new_word)
            print(result)
        else:
            result.append(word)
        
    return " ".join(result)
        