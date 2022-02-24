import heapq
import sys
input = sys.stdin.readline

n = int(input())
queue = []

for i in range(n):
    x = int(input())
    if x == 0:
        if len(queue) == 0:
            print(0)
        else:
            print(abs(heapq.heappop(queue)))
    else:
        heapq.heappush(queue, -x)