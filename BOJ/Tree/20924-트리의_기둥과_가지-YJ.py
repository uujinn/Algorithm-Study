from sys import stdin
from collections import deque
N, R = map(int, stdin.readline().rstrip().split())

graph = {i: dict() for i in range(N+1)}
for _ in range(N-1):
    a, b, d = map(int, stdin.readline().rstrip().split())
    graph[a][b] = d
    graph[b][a] = d


def solution(graph):
    global R
    visited = [False for _ in range(len(graph))]
    q = deque()
    q.append(0, R)

    flag = False

    while q:
        distance, node = q.popleft()

        if distance > longest:
            longest = distance

        if flag != True:
            flag = False
            root = distance

        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                q.append((distance + graph[node][n], n))

        root = longest

    return root, longest - root
