from sys import stdin

# 중위순회 -> x축을 기준으로 왼쪽부터 방문(너비) + depth값 저장

detph_arr = []


def in_order(node, depth):  # 중위 순회에 depth 저장
    if node == -1:  # 리프노드
        return
    in_order(tree[node][0], depth + 1)  # left
    detph_arr.append(depth)
    in_order(tree[node][1], depth + 1)  # right


# MAIN
N = int(stdin.readline())
tree = [[] for _ in range(N+1)]
root_arr = []
for _ in range(N):
    node, left, right = map(int, stdin.readline().rstrip().split())
    root_arr[int(node)] += 1
    root_arr[int(left)] += 1
    root_arr[int(right)] += 1
    tree[node] = [left, right]

root_node = root_arr.index(1)
in_order(root_node, 1)
