import sys
from itertools import permutations, combinations
import math

input = sys.stdin.readline

def primeNum(n):
    init = [True] * n
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if init[i] == True:
            for j in range(i + i, n, i):
                init[j] = False

    return [i for i in range(2, n) if init[i] == True]

K, M = map(int, input().rstrip().split())

com = list(permutations(range(10), K))
prime = primeNum(100001)

primeSum = [False for _ in range(100000)]
primeMul = [False for _ in range(100000)]

for i in range(len(prime) - 1):
    for j in range(i + 1), len(prime):
        if prime[i] + prime[j] < 100000:
            if primeSum[prime[i] + prime[j]] == False:
                primeSum[prime[i] + prime[j]] == True
            else:
                break


answer = 0
answer_ = []

print(answer)