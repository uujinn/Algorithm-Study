from sys import stdin
N = int(stdin.readline())
nodes = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

q = int(stdin.readline())
for _ in range(q):
    t, k = map(int, stdin.readline().split())
    if t == 1:
        print("no" if len(nodes[k])==1 else "yes")
    else:
        print("yes")