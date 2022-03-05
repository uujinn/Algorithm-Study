from heapq import heapify, heappop, heappush, nlargest

h = []
N = int(input())

for _ in range(N):
    numbers = list(map(int, input().split()))
    for num in numbers:
        heappush(h, num)
    
    h = nlargest(N, h)

heapify(h)

print(heappop(h))