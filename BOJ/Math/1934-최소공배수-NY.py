from sys import stdin
def gcdFunc(a,b):
    if b == 0: return a
    else: return gcdFunc(b, a%b)

T = int(stdin.readline())
for _ in range(T):
    A, B = map(int, stdin.readline().split())
    gcd = gcdFunc(A, B)
    lcm = gcd * (A // gcd) * (B // gcd)
    print(lcm)