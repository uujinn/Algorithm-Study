from sys import stdin
from itertools import combinations

T = int(stdin.readline().strip())
for _ in range(T):
    N, M = map(int, stdin.readline().strip().split())
    cnt = 0
    for c in combinations(range(1, M+1), N):
        cnt += 1
    print(cnt)
