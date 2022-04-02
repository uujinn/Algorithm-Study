from sys import stdin

N, W = map(int, stdin.readline().split())
leaf = 0
tree = [[] for _ in range (N + 1)]

for _ in range(N - 1):
    U, V = map(int, stdin.readline().split())
    tree[U].append(V)
    tree[V].append(U)

for i in range(2, N + 1):
    if len(tree[i]) == 1:
        leaf += 1
        
print(W / leaf)