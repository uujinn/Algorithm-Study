from sys import stdin
from collections import deque
N = int(stdin.readline())
q = deque()
for i in range(N):
    command = stdin.readline().split()
    if command[0] == 'push':
        q.append(int(command[1]))
    elif command[0] == 'pop':
        if len(q) == 0: print(-1)
        else: print(q.popleft())
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q) == 0: print(1)
        else: print(0)
    elif command[0] == 'front':
        if len(q) == 0: print(-1)
        else: print(q[0])
    elif command[0] == 'back':
        if len(q) == 0: print(-1)
        else: print(q[-1])