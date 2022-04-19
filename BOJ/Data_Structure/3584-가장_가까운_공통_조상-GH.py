from sys import stdin
input = stdin.readline

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    tree = [0 for _ in range(n+1)]

    for _ in range(n-1):
        p, c = map(int, input().split())
        tree[c] = p
    a, b = map(int, input().split())
    parent_a = [a]
    parent_b = [b]

    temp = a
    while tree[temp]:
        parent_a.append(tree[temp])
        temp = tree[temp]
    temp = b
    while tree[temp]:
        parent_b.append(tree[temp])
        temp = tree[temp]
    idx_a = len(parent_a)-1
    idx_b = len(parent_b)-1

    while parent_a[idx_a] == parent_b[idx_b]:
        idx_a -= 1
        idx_b -= 1

    print(parent_a[idx_a+1])