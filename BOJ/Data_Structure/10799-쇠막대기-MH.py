import sys
from collections import deque

piece = 0
sticks = deque()
str = sys.stdin.readline().rstrip()

for idx, char in enumerate(str):
    if char == '(':
        sticks.append(0)

    elif char == ')':
        sticks.pop()
        
        if str[idx - 1] == '(':       # 레이저일 경우
            piece += len(sticks)
        elif str[idx - 1] == ')':
            piece += 1

print(piece)