# 전위순회어쩌고


K = int(input())
arr = list(map(int, input().split()))
level = [[] for _ in range(K)]


def recur(tree, cnt):
    root = tree[len(tree)//2]

    level[cnt].append(root)

    left = tree[:len(tree)//2]
    right = tree[len(tree)//2+1:]

    if len(tree) == 1:
        return level
    else:
        recur(left, cnt + 1)
        recur(right, cnt + 1)
    return level


for l in recur(arr, 0):
    print(*l)
