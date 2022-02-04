from collections import deque
from sys import stdin

num = int(stdin.readline())

for _ in range(num):
    N, M = map(int,stdin.readline().split())
    queue = deque(map(int,stdin.readline().split()))
    cnt = 0
    
    while queue:
        top = max(queue)
        M -= 1
        pop = queue.popleft()
        if top != pop:
            queue.append(pop)
            if M < 0:
                M = len(queue)-1
        else:
            cnt += 1
            if M == -1:
                print(cnt)
                break