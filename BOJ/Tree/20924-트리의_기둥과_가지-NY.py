import sys
from sys import stdin
sys.setrecursionlimit(int(10**9))

def DFS(visited, nodes, idx, weight):
    max_w = 0
    for child in nodes[idx]:
        if visited[child[0]]: 
            visited[idx] = True
            continue
        w = DFS(visited, nodes, child[0], child[1])
        max_w = max(w, max_w)
    visited[idx] = True
    return max_w + weight

N, R = map(int, stdin.readline().split())
if N == R == 1: 
    print(0,0)
    exit(1)
nodes = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(N-1):
    a, b, d = map(int, stdin.readline().split())
    nodes[a].append([b, d])
    nodes[b].append([a, d])
giga = R
giga_cnt = 0
con_idx = 0
while True:
    if visited[nodes[giga][con_idx][0]]:
        if len(nodes[giga])==1: 
            visited[giga] = True
            break
        else: con_idx += 1
        continue
    if len(nodes[giga]) >= 3 or (visited[nodes[giga][0][0]] and len(nodes[giga]) == 1) or (giga==R and len(nodes[giga])==2): 
        visited[giga] = True
        break
    visited[giga] = True
    giga_cnt += nodes[giga][con_idx][1]
    giga = nodes[giga][con_idx][0]
    con_idx = 0

print(giga_cnt, DFS(visited, nodes, giga, 0))