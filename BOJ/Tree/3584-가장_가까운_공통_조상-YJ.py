from collections import defaultdict
from sys import stdin


T = int(stdin.readline().rstrip())
for _ in range(T):
    N = int(stdin.readline().rstrip())
    tree = defaultdict(list)
    x = y = 0
    for i in range(N):
        if i == N-1:
            x, y = list(map(int, stdin.readline().rstrip().split()))
        else:
            parent, child = map(int, stdin.readline().rstrip().split())
            tree[child] = parent

    x_roots = []
    while x in tree:
        x_roots.append(x)
        x = tree[x]

    # 겹치는 부모 노드 있는지 확인
    while y in tree:
        if y in x_roots:
            break
        y = tree[y]

    print(y)
