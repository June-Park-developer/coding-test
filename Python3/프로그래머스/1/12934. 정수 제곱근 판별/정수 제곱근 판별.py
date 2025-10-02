import math
def solution(n):
    root = math.sqrt(n)
    if root == int(root):
        return (root+1)**2
    else:
        return -1