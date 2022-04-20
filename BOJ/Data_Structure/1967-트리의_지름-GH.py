from heapq import heappush, heappop
import sys

input = sys.stdin.readline
n = int(input())
s = [[] for i in range(n + 1)]

def dijkstra(start):
    d = [100000000 for i in range(n + 1)]
    d[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        we, ne = heappop(heap)
        for n_n, n_w in s[ne]:
            weight = n_w + we
            if weight < d[n_n]:
                d[n_n] = weight
                heappush(heap, [weight, n_n])
    return d

for i in range(1, n):
    p, c, w = map(int, input().split())
    s[p].append([c, w])
    s[c].append([p, w])
d_ = dijkstra(1)

print(max(dijkstra(d_.index(max(d_[1:])))[1:]))