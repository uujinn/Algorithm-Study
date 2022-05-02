import math

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(math.lcm(a, b))

def gcd(x, y):
    while y:
        x, y = y, x % y
        return x

def lcm(x, y):
    return x * y // gcd(x, y)