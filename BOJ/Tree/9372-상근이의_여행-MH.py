from sys import stdin
from collections import deque

def BFS(start, count):
    deq = deque()
    deq.append(start)
    visited[start] = True
    
    while deq:
        if visited.count(True) == N:        # 모든 국가를 다 방문하면
            return count
        
        curr = deq.popleft()
        
        for node in tree[curr]:
            if not visited[node]:
                deq.append(node)
                visited[node] = True
                count += 1


for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    tree = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    
    for _ in range(M):
        a, b = map(int, stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
    
    print(BFS(1, 0))

