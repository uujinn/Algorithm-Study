import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n):
    prime_arr = []
        
    for i in range(2, n + 1):        
        if isPrime(i):
            prime_arr.append(i)
    return len(prime_arr)

print(solution(5))