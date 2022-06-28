from sys import stdin
def cal(n, m):
    if n==m: return 1
    else: return n*cal(n-1, m)//(n-m)
n, m = map(int, stdin.readline().split())
print(cal(n,m))