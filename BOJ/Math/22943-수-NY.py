from sys import stdin
from itertools import permutations

def return_primes(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*2, n+1, i):
                prime[j] = False
    prime_num = []
    for i in range(2, n+1):
        if prime[i]: prime_num.append(i)
    return prime_num

def first(K, selected):
    added = set()
    for s in selected:
        sum_result = sum(s)
        s_sum = str(sum_result)
        exist = True
        if len(s_sum) > 1:
            for i in range(len(s_sum)):
                for j in range(i+1, len(s_sum)):
                    if s_sum[i] == s_sum[j]: 
                        exist = False
                        break
        if not exist: continue
        if sum_result < 10**K and sum_result >= 10**(K-1): added.add(sum_result)
    return added

def second(K, M, primes, selected):
    multiply = set()
    for p in primes:
        if not p % M: continue
        elif p ** 2 < 10**K: multiply.add(p**2)
    for s in selected:
        if s[0] % M and s[1] % M:
            mul_result = s[0] * s[1]
            if mul_result < 10**K and mul_result % M: multiply.add(mul_result)
    return multiply

K, M = map(int, stdin.readline().split())
primes = return_primes(10**K)
selected = list(permutations(primes, 2))
first = first(K, selected)
second = second(K, M, primes, selected)
print(first)
print(second)
print(len(first.intersection(second)))