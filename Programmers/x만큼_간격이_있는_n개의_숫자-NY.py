def solution(x, n):
    return list(i for i in range(x, x*n+(1 if x > 0 else -1), x))