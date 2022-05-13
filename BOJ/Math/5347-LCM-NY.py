from sys import stdin

def gcd(a, b):
    if a % b == 0: return b
    else: 
        b = gcd(b, a%b)
    return b

def lcm(a, b):
    print(a*b//gcd(a,b))

n = int(stdin.readline())
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    if b > a: b,a = a,b
    lcm(a,b)