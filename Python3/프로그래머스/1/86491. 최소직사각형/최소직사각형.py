def solution(sizes):
    smaller = 0
    bigger = 0
    for w, h in sizes:
        big = max(w, h)
        small = min(w, h)
        if big > bigger :
            bigger = big
        if small > smaller :
            smaller = small
    return smaller * bigger