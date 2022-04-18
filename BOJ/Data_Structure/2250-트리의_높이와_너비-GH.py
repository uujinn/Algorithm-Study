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

for _ in range(n):
    node, left, right = map(int, input().split())

    if left != -1:
    if right != -1:

inOrder(root, 0)

maxLevel, maxLevelWidth = 0, 0
print(maxLevel, maxLevelWidth)