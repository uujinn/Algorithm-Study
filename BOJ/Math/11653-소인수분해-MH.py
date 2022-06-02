from pickle import FALSE
from sys import stdin

def get_primes(n):
    length = n // 2 + 1
    arr = [False, False] + [True] * (n // 2 - 1)
    primes = []
    
    for i in range(2, int(length ** 0.5) + 1):
        for j in range(i * 2, length + 1, i):
            arr[j] = False
    
    for idx, is_prime in enumerate(arr):
        if is_prime: primes.append(idx)
    
    return primes


N = int(stdin.readline())
primes = get_primes(N)

while N != 1:
    for prime in primes:
        if N % prime == 0:
            print(prime)
            N //= prime
            break