from sys import stdin

N, W = map(int, stdin.readline().rstrip().split())

tree = {node: [] for node in range(1, N+1)}

for i in range(N-1):
    U, V = map(int, stdin.readline().rstrip().split())
    tree[U].append(V)
    tree[V].append(U)

last_cnt = 0

# 밑 노드들 count
for node, val in tree.items():
    if len(val) == 1 and node != 1:
        last_cnt += 1

print(W / last_cnt)
