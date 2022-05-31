import sys
import math
from itertools import combinations_with_replacement, permutations
from itertools import combinations


def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def check_sum_prime(n):  # 소수 합인지
    for i, j in combinations(primes, 2):
        if i + j == n:
            return True
    return False


def check_multiple_prime(n, m):  # 최대한 나누었을 때 소수 곱인지
    tmp = n
    while (tmp // m) == 0:
        n //= m
    for i, j in combinations_with_replacement(primes, 2):
        if n == i * j:
            return True
    return False


if __name__ == '__main__':
    k, m = map(int, input().split())
    numbers = list(range(10**(k-1), 10**k))  # 가능한 수
    primes = []
    cnt = 0
    for n in numbers:
        if is_prime(n):
            primes.append(n)
        else:
            continue

    for n in numbers:
        if check_sum_prime(n) and check_multiple_prime(n, m):
            cnt += 1

    print(cnt)
