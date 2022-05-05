from sys import stdin
def eratos(m, n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(2*i, n+1, i):
                primes[j] = False
                
    add = 0
    min_n = n
    for i in range(m, n+1):
        tmp = primes[i]
        if tmp:
            if i < min_n: min_n = i
            add += i
    if not add and min_n == n: print(-1)
    else:
        print(add)
        print(min_n)

M = int(stdin.readline())
N = int(stdin.readline())
eratos(M, N)