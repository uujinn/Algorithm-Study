def solution(a, b):
    if a > b: a, b = b, a
    return a + a * (b - a) + sum([i for i in range(b - a + 1)])