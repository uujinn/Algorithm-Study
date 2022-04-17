from sys import stdin
from collections import deque
T = int(stdin.readline())


def bfs(start, plane):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        if visited.count(True) == N:
            return plane

        pos = q.popleft()

        for p in graph[pos]:
            if not visited[p]:
                q.append(p)
                plane += 1
                visited[p] = True


for _ in range(T):
    N, M = map(int, stdin.readline().rstrip().split())

    visited = [False] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(1, 0))
