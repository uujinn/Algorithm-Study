from heapq import heappop, heappush, nlargest
from sys import stdin

h = []
N = int(stdin.readline())

max_numbers = []

for _ in range(N):
    numbers = list(map(int, stdin.readline().split()))
    for num in numbers:
        heappush(h, num)
    
    max_numbers = nlargest(5, h)

print(max_numbers[-1])
    