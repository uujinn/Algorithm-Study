from sys import stdin

def is_prime(num):
    primes = [False, False] + [True] * (num - 1)
    
    for i in range(2, int(num ** 0.5) + 1):
        if primes[i]:
            for j in range(2 * i, num + 1, i):
                primes[j] = False
                
    return primes


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
is_prime_arr = is_prime(max(nums))

prime_nums = []
for num in set(nums):
    if is_prime_arr[num]:
        prime_nums.append(num)
        
answer = 1
for num in prime_nums:
    answer *= num

print(answer if prime_nums else -1)