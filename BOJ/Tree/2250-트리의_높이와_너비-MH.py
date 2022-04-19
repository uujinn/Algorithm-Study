from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def inorder(node, depth):
    if node == -1:
        return
    inorder(tree[node][0], depth + 1)       # left
    level.append(depth)
    inorder(tree[node][1], depth + 1)       # right
    
    
N = int(stdin.readline())
tree = [0] * (N + 1)
childs = [False] * (N + 1)                  # root 찾기 위함
level = [0]                                 # 인덱스 맞추기 위해 0번째에 0

childs[0] = True                            # 0번째는 사용하지 않음
for _ in range(N):
    node, left, right = map(int, stdin.readline().split())
    tree[node] = (left, right)
    
    # root 찾기 위해 부모 node가 있는 node는 True로 바꿔줌
    if left != -1: childs[left] = True
    if right != -1: childs[right] = True
# print(tree)
# [0, (2, 3), (4, 5), (6, 7), (8, -1), (9, 10), (11, 12), (13, -1),
# (-1, -1), (14, 15), (-1, -1), (16, -1), (-1, -1), (17, -1),
# (-1, -1), (18, -1), (-1, -1), (-1, 19), (-1, -1), (-1, -1)]

# print(childs)
# [True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

root = childs.index(False)                  # 부모node가 없는 node의 인덱스 = root의 인덱스
inorder(root, 1)                            # 각 node의 level을 찾기 위한 중위순회
# print(level)
# [0, 4, 3, 2, 5, 4, 6, 5, 3, 4, 1, 5, 4, 3, 4, 2, 5, 6, 4, 3]

level_reverse = level[::-1]
# print(level_reverse)

depth = max(level)                          # tree의 가장 깊은 level
width = [0] * (depth + 1)
for i in range(1, depth + 1):
    width[i] = (N - level_reverse.index(i)) - level.index(i) + 1
# print(width)
# [0, 1, 13, 18, 18, 13, 12]

print('{} {}'.format(width.index(max(width)), max(width)))