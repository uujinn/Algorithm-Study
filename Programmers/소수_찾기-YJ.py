import math


def solution(n):
    answer = 0
    for i in range(2, n+1):
        if isPrime(i):
            answer += 1
    return answer


def isPrime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True
