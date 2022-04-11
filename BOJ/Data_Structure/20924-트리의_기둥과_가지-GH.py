from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**9)

input = stdin.readline

N, R = map(int, input().split())
tree = defaultdict(dict)
for _ in range(N-1):
    a, b, w = map(int, input().split())
    tree[a][b] = w
    tree[b][a] = w

# maxbranch...를 찾아봐요...

# 기가 노드까지 길이 찾기
gigaNode = R
gigaLen = 0
while len(tree[gigaNode])==1:
    node, w = list(tree[gigaNode].items())[0]
    del tree[node][gigaNode]
    gigaLen += w
    gigaNode = node

print('{} {}'.format(gigaLen, maxBranch))