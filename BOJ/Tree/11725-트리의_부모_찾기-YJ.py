from collections import deque
from sys import stdin

n = int(input())

graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)] # 부모 노드

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if parent[i] == 0:
                parent[i] = v
                queue.append(i)

for i in range(n-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1) # 트리의 루트 = 1

for i in parent[2:]:
    print(i)