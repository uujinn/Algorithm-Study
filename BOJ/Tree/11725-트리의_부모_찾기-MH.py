import sys
sys.setrecursionlimit(10 ** 6)          # 재귀 반복 횟수 늘려줌

def DFS(curr):
    for next in tree[curr]:
        if visited[next]:               # 이 노드를 방문한 적이 있다면 부모 노드
            continue
            
        tree_parent[next] = curr
        visited[next] = True
        DFS(next)                       # curr의 자식 노드인 next의 자식 노드 탐색


N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]       # 2차원 배열에서 0번째 배열은 쓰지 않음 (1 ~ N번째 배열만 사용)
tree_parent = [0] * (N + 1)             # 각 노드의 부모 노드 저장
visited = [False] * (N + 1)             # 각 노드의 방문 여부 저장 (부모 노드인지 판단 위함)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)                   # 어느 노드가 부모인지 자식인지 모름
    tree[b].append(a)                   # -> 연결된 정점 모두 저장

# print(tree)
# [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

visited[1] = True                       # 루트 1
DFS(1)

for i in range(2, N + 1):
    print(tree_parent[i])