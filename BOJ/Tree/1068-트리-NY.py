import sys
sys.setrecursionlimit(int(100000))

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def DFS(root, visited, target):
    if root is None or visited[root.data]: return
    else:
        visited[root.data] = True
        if root.data == target:
            root = None
            return
        if root.left is None and root.right is None:
            cnt[0] += 1
            return
    DFS(root.left, visited, target)
    if root.left is None and root.right is None:
        cnt[0] += 1
    DFS(root.right, visited, target)

N = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

Tree = [0] * N
visited = [False] * N
cnt = [0]

Tree[0] = Node(0)

for idx, parent in enumerate(parents):
    if idx == 0: continue
    Tree[idx] = Node(idx)
    if Tree[parent].left is None:
        Tree[parent].left = Tree[idx]
    else: Tree[parent].right = Tree[idx]

DFS(Tree[0], visited, target)

print(cnt[0])