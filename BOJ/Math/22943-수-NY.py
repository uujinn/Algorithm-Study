from sys import stdin
from itertools import permutations

def return_primes(n):
    prime = [True] * (n)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*2, n, i):
                prime[j] = False
    return prime

def first(num, prime):
    for i in range(2, num//2+1):
        j = num - i
        if i != j and prime[i] and prime[j]: return True
    return False

def second(num, M, prime):
    tmp = num
    while tmp//M: tmp//=M
    div = tmp % M
    for i in range(2, int(div**0.5)+1):
        if div % i == 0:
            if prime[i] and prime[div//i]: return True
    return False

K, M = map(int, stdin.readline().split())
cnt = 0
prime = return_primes(10**K)
for num in permutations(['0', '1', '2', '3', '4', '5', '6', '7','8', '9'], K):
    if num[0] == '0': continue
    number = int(''.join(num))
    if first(number, prime) and second(number, M, prime): cnt += 1
print(cnt)