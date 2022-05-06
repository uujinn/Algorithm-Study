from sys import stdin
def find_prime(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not prime[i]:
            for j in range(i*2, n, i):
                prime[j] = False
    primes = []
    for i in range(2, n+1):
        if prime[i]: primes.append(i)
    return primes

N = int(stdin.readline())
primes = find_prime(N)
i = 0
while N != 1:
    if not N % primes[i]: 
        N //= primes[i]
        print(primes[i])
    else: i += 1