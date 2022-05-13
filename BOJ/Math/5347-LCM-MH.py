from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def GCD(x, y):
    if y == 0:
        return x
    return GCD(y, x % y)

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    gcd = GCD(a, b)
    print(a * b // gcd)