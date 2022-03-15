from collections import deque
import sys

N = int(sys.stdin.readline())
q = deque(enumerate(map(int, sys.stdin.readline().split())))
result = []

while q:
    num, i = q.popleft()
    result.append(num + 1)
    
    if i > 0:
        q.rotate(-(i-1))
    else:
        q.rotate(-i)
        
for x in result:
    print(x, end = ' ')