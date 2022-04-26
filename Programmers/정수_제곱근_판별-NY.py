from math import sqrt
def solution(n):
    if sqrt(n) - float(round(sqrt(n))) != 0: return -1
    else: return (int(sqrt(n)) + 1)**2