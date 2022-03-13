from sys import stdin
from collections import defaultdict

marathoners = defaultdict(int)
N = int(stdin.readline())

for _ in range(N):
    marathoners[stdin.readline().rstrip()] += 1

for _ in range(N - 1):
    marathoners[stdin.readline().rstrip()] -= 1
    
for k, v in marathoners.items():
    if v == 1:
        print(k)