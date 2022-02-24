from queue import PriorityQueue
from sys import stdin
N = int(stdin.readline())
q = PriorityQueue()
for _ in range(N):
    cmd = int(stdin.readline())
    if not cmd: #cmd가 0일때
        if q.empty(): print(0)
        else:
            print(q.get()[1])
    else: #자연수가 입력 되었을 때
        q.put((-cmd, cmd))