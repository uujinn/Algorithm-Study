from sys import stdin

N = int(stdin.readline())
graph = {} # 왼쪽 자식, 오른쪽 자식

for i in range(N):
    p, l, r = stdin.readline().rstrip().split() # 부모, 왼쪽 자식, 오른쪽 자식
    graph[p] = [l, r] # {부모 노드: [자식노드, 자식노드]}

# print(graph)

def pre(A, graph):
    # .은 무시
    if A in graph:
        print(A, end="")
        pre(graph[A][0], graph)
        pre(graph[A][1], graph)

def middle(A, graph):
    if A in graph:
        middle(graph[A][0], graph)
        print(A, end="")
        middle(graph[A][1], graph)

def after(A, graph):
    if A in graph:
        after(graph[A][0], graph)
        after(graph[A][1], graph)
        print(A, end="")

pre('A', graph)
print()
middle('A', graph)
print()
after('A', graph)