import math


def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return (math.sqrt(n) + 1) ** 2
    else:
        return -1
