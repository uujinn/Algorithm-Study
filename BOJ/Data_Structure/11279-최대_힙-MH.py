from sys import stdin
import heapq

heap = []
n = int(stdin.readline())

for _ in range(n):
    temp = int(stdin.readline())

    if temp == 0 and not heap:
        print(0)
    elif temp == 0 and heap:
        print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -temp)