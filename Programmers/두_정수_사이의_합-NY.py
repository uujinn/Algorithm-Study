def solution(a, b):
    tmp = a
    a = a if a < b else b
    b = b if b >= tmp else tmp
    return sum(list(i for i in range(a, b+1)))