import heapq
from sys import stdin

N = int(stdin.readline())
heap = []

for _ in range(N):
  x = int(stdin.readline())

  if x == 0:
    if heap:
      print(heapq.heappop(heap)[1])
    else:
      print(0)

  else:
    heapq.heappush(heap, (abs(x), x))