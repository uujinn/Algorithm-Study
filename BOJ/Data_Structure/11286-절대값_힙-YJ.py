import heapq
from sys import stdin

input = stdin.readline
h = []

for _ in range(int(input())):
    x = int(input())
    if x != 0: 
        heapq.heappush(h, (abs(x), x))
    else:
        if not h: # 최소힙이 비어있다면
            print(0)
        else:
            print(heapq.heappop(h)[1])