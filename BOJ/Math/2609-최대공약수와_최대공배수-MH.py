from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def GCD(x, y):
    if y == 0:
        return x
    return GCD(y, x % y)


a, b = map(int, stdin.readline().split())
x, y = max(a, b), min(a, b)

# 최대공약수
gcd = GCD(x, y)
print(gcd)

# 최소공배수
print(a * b // gcd)