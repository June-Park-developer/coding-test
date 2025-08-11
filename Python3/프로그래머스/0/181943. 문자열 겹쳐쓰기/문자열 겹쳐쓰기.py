def solution(my_string, overwrite_string, s):
    n = len(overwrite_string)
    
    answer = ''
    answer += my_string[:s]
    answer += overwrite_string
    answer += my_string[s+n:]
    return answer