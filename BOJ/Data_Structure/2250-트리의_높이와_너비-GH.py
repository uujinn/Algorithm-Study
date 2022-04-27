from sys import stdin

input = stdin.readline

def inOrder(node, level):
    global idx
    left, right = graph[node].values()
    if left != -1:
        inOrder(left, level + 1)

    levelOfNode[level].append(idx)
    idx += 1

    if right != -1:
        inOrder(right, level + 1)


n = int(input())
graph = dict()
parent_check = [False] * n
levelOfNode = [[] for _ in range(n)]
idx = 1

for _ in range(n):
    node, left, right = map(int, input().split())

    if left != -1:
        parent_check[left - 1] = True
    if right != -1:
        parent_check[right - 1] = True
    graph[node] = {'l': left, 'r': right}

root = parent_check.index(False) + 1

inOrder(root, 0)

maxLevel, maxLevelWidth = 0, 0

for level, nodes in enumerate(levelOfNode):
    if nodes:
        width = max(nodes) - min(nodes) + 1
        if maxLevelWidth < width:
            maxLevelWidth = width
            maxLevel = level + 1

print(maxLevel, maxLevelWidth)