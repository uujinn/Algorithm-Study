from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
    
def DFS(root):
    global answer
    
    if not tree[root]:      # tree[root]의 원소가 없다면 (자식 노드가 없다면)
        answer += 1
    else:                   # tree[root]의 원소가 있다면
        for node in tree[root]:
            DFS(node)


N = int(stdin.readline())
nodes = list(map(int, stdin.readline().split()))
deleted = int(stdin.readline())

answer = 0
tree = [[] for _ in range(N)]
   
for i in range(N):
    if nodes[i] == -1:
        root = i
    else:
        tree[nodes[i]].append(i)        
# tree : [[1, 2], [3, 4], [], [], []]
# 0을 부모로 가지는 자식 노드 인덱스 : 1, 2
# 1을 부모로 가지는 자식 노드 인덱스 : 3, 4

for i, node in enumerate(tree):
    if deleted in node:
        tree[i].remove(deleted)
# deleted == 2 일 때, 2번째 인덱스의 노드(0을 부모로 가지는 노드) 삭제
# tree : [[1], [3, 4], [], [], []]

if deleted != root:         # 삭제된 노드가 root가 아니면 DFS로 카운트
    DFS(root)
print(answer)