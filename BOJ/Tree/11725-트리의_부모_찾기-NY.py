from sys import stdin
from collections import deque

def BFS(Connections, visited, answer):
    q = deque([1])
    visited[1] = True #처음 1은 루트이고, 정답에서 출력될 필요가 없으므로 미리 처리
    while q: #큐가 빌때까지 반복
        parent = q.popleft() #popleft한 값은 무조건 부모 노드
        for c in Connections[parent]: #부모노드와 연결되어 있는 값들을 모아둔 배열 반복문 돌면서 확인
            if not visited[c]: #만약 방문한 적 없다면
                answer[c] = parent #c번째 숫자의 부모 노드는 parent
                q.append(c)
                visited[c] = True

N =  int(stdin.readline())
Connections = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, stdin.readline().split())
    Connections[a].append(b) #a번째 인덱스에 값 추가. 
    Connections[b].append(a) #양방향으로 추가.

BFS(Connections, visited, answer)

for i in range(2, N+1):
    print(answer[i])