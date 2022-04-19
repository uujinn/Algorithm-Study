from sys import stdin
#더 이상 물이 움직이지 않을 떄 == 모든 leaf 노드들에 물이 가득 들어가있을떄
N, W = map(int, stdin.readline().split())
nodes = [[] for _ in range(N+1)]
leaf_cnt = 0
for _ in range(N-1):
    u, v = map(int, stdin.readline().split())
    nodes[u].append(v)
    nodes[v].append(u)

for i in range(2, N+1):
    if len(nodes[i]) == 1: leaf_cnt += 1

print(W/leaf_cnt)