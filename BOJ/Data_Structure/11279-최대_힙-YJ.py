import heapq
from sys import stdin

N = int(stdin.readline())
heap = []

for _ in range(N):
    x = int(stdin.readline())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))

    else:
        heapq.heappush(heap, -x)
