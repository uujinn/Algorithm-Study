from collections import deque


def solution(priorities, location):
    n = len(priorities)
    q = deque()

    for i in range(n):
        q.append((i, priorities[i]))

    high_priority = max(q, key=lambda x: x[1])[1]

    rank = 1
    while q:
        high_priority = max(q, key=lambda x: x[1])[1]
        idx, job = q.popleft()

        if job == high_priority:
            if idx == location:
                return rank
            else:
                rank += 1
        else:
            q.append((idx, job))
