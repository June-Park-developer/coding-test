def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    actual_reserve = sorted(list(reserve_set - lost_set))
    actual_lost = sorted(list(lost_set - reserve_set))
    
    for r in actual_reserve:
        if (r-1) in actual_lost:
            actual_lost.remove(r-1)
        elif (r+ 1) in actual_lost:
            actual_lost.remove(r+1)
            
    return n - len(actual_lost)
        