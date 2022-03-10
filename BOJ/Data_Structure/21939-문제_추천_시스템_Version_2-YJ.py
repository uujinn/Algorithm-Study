from collections import defaultdict
from sys import stdin
from heapq import heappop, heappush


N = int(stdin.readline().rstrip())

max_h = [] # 최대 힙
min_h = [] # 최소 힙

for _ in range(N):
    