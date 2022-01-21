from sys import stdin
from collections import deque

N = int(stdin.readline())

cards = deque([i+1 for i in range(N)])


while len(cards)>1:
    cards.popleft()
    cards.rotate(-1)

print(cards[0])