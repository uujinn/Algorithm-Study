from sys import stdin
    
def DFS(root, answer):
    if tree[root] == '':
        answer += 1
        return
    for node in tree[root]:
        DFS(node)


N = int(stdin.readline())
nodes = list(map(int, stdin.readline().split()))
deleted = int(stdin.readline())

answer = 0
tree = [[] for _ in range(N)]
   
for i in range(len(tree)):
    if nodes[i] == -1:
        root = i
    elif i == deleted:
        continue
    tree[nodes[i]].append(i)
        
print(tree)

if root != deleted:
    DFS(tree, answer)
print(answer)