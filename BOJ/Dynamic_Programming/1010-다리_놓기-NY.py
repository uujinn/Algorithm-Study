import sys
from sys import stdin
sys.setrecursionlimit(int(10**9))
def f(N, M, recur):
    ans = 0
    if N==M: return 1
    if N==1 and recur:
        while M != 1:
            ans += M
            M -= 1
        return ans
    else:
        while N!=M:
            M -= 1
            if N-1 == 1: ans += f(N-1, M, True)
            else: ans += f(N-1, M, False)
        return ans

T = int(stdin.readline())
for _ in range(T):
    N, M = map(int, stdin.readline().split())
    print(f(N,M, False))