import heapq
from sys import stdin
N = int(stdin.readline())
heap = []
for _ in range(N):
    cmd = int(stdin.readline())
    if cmd: heapq.heappush(heap, [abs(cmd), cmd])
    else:
        if not heap: print(0)
        else: print(heapq.heappop(heap)[1])