def solution(s):
    new = s.lower()
    if new.count('p') != new.count('y'):
        return False
    return True

