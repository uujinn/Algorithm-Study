from collections import deque
from sys import stdin
N = int(stdin.readline())
cards = deque(i for i in range(N, 0, -1))
while len(cards) >= 1:
    if len(cards) == 1: 
        print(cards[0])
        break
    else:
        cards.pop()
        cards.appendleft(cards.pop())