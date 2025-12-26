def solution(brown, yellow):
    for i in range (1, int(yellow**(0.5))+1):
        if yellow / i == yellow // i:
            yellow_h = i
            yellow_w = yellow // i
            if brown == (2 * yellow_w + 2 * yellow_h + 4) :
                return [yellow_w+2, yellow_h+2]