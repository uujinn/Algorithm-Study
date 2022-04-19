'''
트리의 지름을 구하는 방법은 다음과 같다.
임의의 노드 x에서 가장 먼 거리에 있는 노드 a를 찾는다.
노드 a에서 가장 먼 거리에 있는 노드 b를 찾는다.
트리의 지름은 a와 b를 연결하는 경로이다.

지름 = a - b
'''

from sys import stdin

n = int(stdin.readline().rstrip())


tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, stdin.readline().rstrip().split())
    tree[a].append([b, c])
    tree[b].append([a, c])


def dfs(x):
    visited = [0] * (n+1)
    queue = []
    queue.append(x)
    visited[x] = 1
    max_node = 0
    max_length = 1
    while queue:
        x = queue.pop()
        for node, weight in tree[x]:
            if not visited[node]:
                visited[node] = visited[x] + weight  # 누적
                queue.append(node)
                if visited[node] > max_length:
                    max_length = visited[node]  # 갱신
                    max_node = node

    return max_node, max_length-1


a = dfs(1)[0]  # 루트 노드는 항상 1
length = dfs(a)[1]

print(length)
