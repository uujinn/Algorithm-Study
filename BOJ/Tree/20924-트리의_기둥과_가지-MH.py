from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10 ** 6)

def getMaxBranch(tree, root):
    if root not in tree:
        return 0
    
    max_branch = 0
    for node, d in tree[root].items():        
        del tree[node][root]
        branch = d + getMaxBranch(tree, node)
        
        if branch > max_branch:
            max_branch = branch
    return max_branch


N, R = map(int, stdin.readline().split())
tree = defaultdict(dict)

for _ in range(N - 1):
    a, b, d = map(int, stdin.readline().split())
    tree[a][b] = d
    tree[b][a] = d

# print(tree)
# {1: {2: 1}, 2: {1: 1, 3: 2}, 3: {2: 2, 4: 3}, 4: {3: 3, 5: 1, 9: 2, 10: 3},
# 5: {4: 1, 6: 2, 8: 1}, 6: {5: 2, 7: 1}, 7: {6: 1}, 8: {5: 1}, 9: {4: 2},
# 10: {4: 3, 11: 1, 12: 3}, 11: {10: 1}, 12: {10: 3}})
# node 1은 node 2와 1 거리로 연결
# dnoe 2는 node 1과 1 거리로 연결, node 3과 2 거리로 연결 ...

# 나무의 기둥의 거리
giga_node, pole_len = R, 0
while len(tree[giga_node]) == 1:
    node, d = list(tree[giga_node].items())[0]
    
    del tree[node][giga_node]
    pole_len += d
    giga_node = node

# 가장 긴 가지의 길이
max_branch = getMaxBranch(tree, giga_node)

print('{} {}'.format(pole_len, max_branch))