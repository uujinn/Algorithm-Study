from sys import stdin
from collections import deque

N = int(stdin.readline())

queue = deque([])

for i in range(N):
    command = stdin.readline().split()

    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if len(queue)==0 else 0)
    elif command[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])