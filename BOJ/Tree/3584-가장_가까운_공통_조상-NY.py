from sys import stdin

def find(x, nodes):
    parents = [x]
    while len(nodes[x]):
        parents.append(nodes[x][0])
        x = nodes[x][0]
    return parents

def search(x, y, nodes):
    x_parents = find(x, nodes)
    y_parents = find(y, nodes)
    for x_p in x_parents:
        for y_p in y_parents:
            if x_p == y_p: return x_p

T = int(stdin.readline())
parents = []
for _ in range(T):
    N = int(stdin.readline())
    nodes = [[] for _ in range(N+1)]
    for i in range(N):
        A, B = map(int, stdin.readline().split())
        if i < N-1: 
            nodes[B].append(A)
        else: #공통조상 찾아야 하는 노드들
            parents.append(search(A, B, nodes))
            
for parent in parents:
    print(parent)