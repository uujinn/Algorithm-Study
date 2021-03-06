from sys import stdin

def getPrimeNum(b):
    array = [False, False] + [True] * (b - 1)
    
    m = int(b ** 0.5)
    for i in range(2, m + 1):
        if array[i]:
            for j in range(2 * i, b + 1, i):
                array[j] = False
    return array


M = int(stdin.readline())
N = int(stdin.readline())
primes = getPrimeNum(N)
answer = []

if N == M and primes[N]:
    answer.append(N)
else:
    for i in range(M, N + 1):
        if primes[i]:
            answer.append(i)

if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)