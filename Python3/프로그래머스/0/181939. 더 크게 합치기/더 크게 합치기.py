def solution(a, b):
    one = int (f"{a}" + f"{b}")
    two = int (f"{b}" + f"{a}")
    
    if one >= two :
        return one
    else :
        return two