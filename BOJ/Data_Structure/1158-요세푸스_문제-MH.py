import sys
from collections import deque

deq = deque()
josephus = []

n, k = (sys.stdin.readline()).split(' ')
for i in range(int(n)):
    deq.append(i + 1)

while (deq):
    deq.rotate(-(int(k) - 1))
    josephus.append(str(deq.popleft()))

print('<' + ", ".join(josephus) + '>')

# 104ms