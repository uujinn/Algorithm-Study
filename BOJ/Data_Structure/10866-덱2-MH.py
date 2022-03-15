from collections import deque
import sys

deq = deque()
for i in range(int(sys.stdin.readline())):
    str = sys.stdin.readline().rstrip().split()

    if 'push_front' in str:        deq.appendleft(str[1])
    elif 'push_back' in str:        deq.append(str[1])
    elif 'pop_front' == str[0]:        print(-1) if len(deq) == 0 else print(deq.popleft())
    elif 'pop_back' == str[0]:        print(-1) if len(deq) == 0 else print(deq.pop())
    elif 'size' == str[0]:        print(len(deq))
    elif 'empty' == str[0]:        print(1) if len(deq) == 0 else print(0)
    elif 'front' == str[0]:        print(-1) if len(deq) == 0 else print(deq[0])
    elif 'back' == str[0]:        print(-1) if len(deq) == 0 else print(deq[-1])

# https://www.acmicpc.net/source/38034469