import math
from itertools import permutations
MAX = 1000001
is_prime = [True] * MAX


def check_sum_prime(n):
    for i in range(2, n // 2 + 1):
        if i != n - i and is_prime[i] and is_prime[n - i]:
            return True
    return False


def sub_multiple(num, k):
    if num < k:
        return num
    while 1:
        if(num % k != 0):
            return num
        num //= k
    return num


def check_multiple_prime(n, k):
    result = sub_multiple(n, k)
    for i in range(2, int(math.sqrt(result)) + 1):
        if result % i == 0 and is_prime[i] and is_prime[result // i]:
            return True
    return False


is_prime[0] = False
is_prime[1] = False
is_prime[2] = True
for i in range(int(math.sqrt(MAX)) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX, i):
            is_prime[j] = False

K, M = map(int, input().split())
ans = 0
for num in permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], K):
    if(num[0] == '0'):
        continue
    num = int(''.join(num))
    if(check_sum_prime(num)):
        if(check_multiple_prime(num, M)):
            ans += 1

print(ans)
