from sys import stdin
def gcd(a, b):
    if a < b: a,b = b, a
    if b == 0: return a
    else: return gcd(b, a%b)

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
X = int(stdin.readline())
ans = 0
cnt = 0
for a in A:
    if a == X: continue
    if gcd(a, X) == 1: 
        ans += a
        cnt += 1

print(ans/cnt)
