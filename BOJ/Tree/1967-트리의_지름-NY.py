from sys import stdin
from collections import deque

n = int(stdin.readline())
nodes = [{} for _ in range(n+1)]
visited = [False] * n+1

def BFS(nodes, visited, weights):
    q = deque([1])
    visited[1] = True
    while q:
        parent = q.popleft()
        for child, value in nodes[parent].items():
            if not visited[child]:
                

for _ in range(n-1):
    parent, child, weight = map(int, stdin.readline().split())
    nodes[parent][child] = weight #자식 노드 값: 가중치값
    #nodes[child].append(parent) #필요한가..?
    

'''
트리의 지름을 구하는 방법은 다음과 같다.
임의의 노드 x에서 가장 먼 거리에 있는 노드 a를 찾는다.
노드 a에서 가장 먼 거리에 있는 노드 b를 찾는다.
트리의 지름은 a와 b를 연결하는 경로이다.

지름 = a - b 
유진언니가 알려줬는데 오늘 시간이 너무 부족해요... 
'''