from sys import stdin

def get_Knums(K):
    Knums = []
    start, end = int('1' + '0' * (K - 1)), int('9' + '9' * (K - 1))
    
    for i in range(start, end + 1):
        if len(str(i)) == len(set(str(i))):     # 숫자를 한 번씩만 사용
            Knums.append(i)
        
    return Knums


def get_primes(n):
    arr = [False, False] + [True] * (n - 1)
    primes = []
    
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i * 2, n + 1, i):
            arr[j] = False
    
    for idx, is_prime in enumerate(arr):
        if is_prime: primes.append(idx)
    
    return primes

    
K, M = map(int, stdin.readline().split())
Knums = get_Knums(K)
primes = get_primes(max(Knums))