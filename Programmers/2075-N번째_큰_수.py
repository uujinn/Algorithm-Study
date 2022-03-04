from sys import stdin
from heapq import heappop, heappush

heap = []       # 최대 힙
N = int(stdin.readline())

for _ in range(N):
    for num in map(int, stdin.readline().split()):
        heappush(heap, num * (-1))

for _ in range(N - 1):
    heappop(heap)

print(heappop(heap) * (-1))