import math

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(math.lcm(a, b))

def gcd(a, b):
    while b:
        x, y = y, x % y
        return x

def lcm(a, b):
    return a * b // gcd(a, b)
