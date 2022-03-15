import sys
from collections import deque

card = deque()
n = int(sys.stdin.readline())

for i in range(0, n):
    card.append(i + 1)

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])