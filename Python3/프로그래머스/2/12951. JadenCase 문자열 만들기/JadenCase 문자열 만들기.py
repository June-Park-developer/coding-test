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


# 가져가야 하는 것
## split 문법, join 문법
## 문자열은 불변이기 때문에 upper(), lower() 해도 원래 문자열이 바뀌지는 않음
