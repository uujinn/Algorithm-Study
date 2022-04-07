from email.policy import default
from sys import stdin


def dfs(x):
    visited[x] = True
    for y in tree[x]:
        if visited[y] == False:
            dfs(y)


T = int(stdin.readline().rstrip())
for _ in range(T):
    N = int(stdin.readline().rstrip())
    tree = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    depth = [0 for _ in range(N+1)]
    root = 0
    for i in range(N+1):
        if i == N:
            x, y = map(int, stdin.readline().rstrip().split())
        else:
            parent, child = map(int, stdin.readline().rstrip().split())
            tree[child].extend([parent])

    for idx, l in enumerate(tree):
        if l == [] and idx != 0:
            root = idx  # 루트 노드는 부모가 없음
            print(root)
            break

    dfs(root)
