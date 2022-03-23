
N = int(input())
tree = [[] for _ in range(N)]
parents = list(map(int, input().split()))
del_node = int(input())


def dfs(root):
    global cnt
    if not tree[root]:  # tree[root]가 비어있다면 해당 노드의 자식노드가 없는 것임
        cnt += 1  # 리프 노드
    else:
        for node in tree[root]:  # 리프 노드가 아닌 경우
            dfs(node)  # 또 돌아


for i, parent in enumerate(parents):
    if parent == -1:
        root = i  # 루트 노드
    else:
        tree[parent].append(i)  # 자식 노드 추가
        # [[1, 2], [3, 4], [], [], []]

# print(tree)

# tree[del_node] = []

for i, node in enumerate(tree):
    if del_node in node:  # 노드 삭제
        tree[i].remove(del_node)
# print(tree)

cnt = 0
# dfs로 돌면서 리프노드 개수 구함
if del_node != root:
    dfs(root)

print(cnt)
