from collections import deque
from sys import stdin

input = stdin.readline

q = deque()

N = int(input())

for _ in range(N):
    command = input().split()

    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
