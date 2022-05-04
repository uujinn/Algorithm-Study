def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


def lcm(n, m):
    return n * m // gcd(n, m)


def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer
