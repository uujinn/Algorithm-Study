from sys import stdin
from collections import deque

n = int(stdin.readline())
balloons = deque(map(int, stdin.readline().split()))
sequence = deque([str(i + 1) for i in range(n)])
answer = ''

for i in range(n):
    answer += sequence.popleft() + ' '
    move = balloons.popleft()
    
    balloons.rotate(-move + 1 if move > 0 else -move)
    sequence.rotate(-move + 1 if move > 0 else -move)
    
print(answer.rstrip())