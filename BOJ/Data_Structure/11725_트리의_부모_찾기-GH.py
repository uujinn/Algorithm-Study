import sys
sys.setrecursionlimit(10 ** 6)

def DFS(x):
    visit[x] = True
    for i in graph[x]:
        if not visit[i]:
            answer[i] = x
            DFS(i)

N = int(input())

graph = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
answer = [1 for _ in range(N+1)]


for i in range(N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in graph:
    i.sort()

DFS(1)

for i in range(2, len(answer)):
    print(answer[i])