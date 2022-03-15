from sys import stdin
from collections import deque
N = int(stdin.readline())
deq = deque()
for _ in range(N):
    command = stdin.readline().split()
    if command[0] == 'push_front': deq.appendleft(command[1])
    elif command[0] == 'push_back': deq.append(command[1])
    elif command[0] == 'pop_front': print(-1 if len(deq)==0 else deq.popleft())
    elif command[0] == 'pop_back': print(-1 if len(deq)==0 else deq.pop())
    elif command[0] == 'size': print(len(deq))
    elif command[0] == 'empty': print(1 if len(deq)==0 else 0)
    elif command[0] == 'front': print(-1 if len(deq)==0 else deq[0])
    elif command[0] == 'back': print(-1 if len(deq)==0 else deq[-1])