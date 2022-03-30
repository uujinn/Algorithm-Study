from sys import stdin

n = int(stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, stdin.readline().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)


q = int(stdin.readline())
for _ in range(q):
    t, k = map(int, stdin.readline().rstrip().split())

    if t == 2:
        print("yes")
    else:
        if len(tree[k]) < 2:  # 연결된 노드가 1개거나 0개면
            print("no")
        else:
            print("yes")
