from sys import stdin

def getPrimeNums(n):
    primes = [False] * 2 + [True] * (n - 1)
    
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    
    return primes    


N = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
primes = getPrimeNums(max(numbers))

answer = 0
for number in numbers:
    if primes[number]:
        answer += 1

print(answer)