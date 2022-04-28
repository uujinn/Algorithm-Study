from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**9)

input = stdin.readline


def getMaxBranch(tree, root):
    if root not in tree: return 0

    maxBranch = 0
    for node, w in tree[root].items():
        del tree[node][root]
        branch = w + getMaxBranch(tree, node)
        if branch > maxBranch :
            maxBranch = branch
    return maxBranch

N, R = map(int, input().split())
tree = defaultdict(dict)
for _ in range(N-1):
    a, b, w = map(int, input().split())
    tree[a][b] = w
    tree[b][a] = w

gigaNode = R
gigaLen = 0

while len(tree[gigaNode]) == 1:
    node, w = list(tree[gigaNode].items())[0]
    del tree[node][gigaNode]
    gigaLen += w
    gigaNode = node

maxBranch = getMaxBranch(tree, gigaNode)
print('{} {}'.format(gigaLen, maxBranch))