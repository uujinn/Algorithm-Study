from collections import deque

n, k = map(int, input().split())
S = list(map(int, input().split()))
q = deque()
delete = 0
cnt = 0

for i in S:
    q.append(i)

    if i % 2 == 0:
        cnt += 1
    else:
        delete += 1
    if delete > k:
        num = q.popleft()
        if num % 2 == 1:
            delete -= 1
        else:
            cnt -= 1
