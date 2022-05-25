import math


def is_sosu(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def lcm(x, y):
    return x * y // math.gcd(x, y)


N = int(input())
arr = list(set(list(map(int, input().split()))))


lcm_value = 1
cnt = 0
for n in arr:
    if is_sosu(n):
        lcm_value = lcm(n, lcm_value)
        cnt += 1
    else:
        continue

if cnt == 0:
    print(-1)
else:
    print(lcm_value)
