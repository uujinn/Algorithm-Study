from sys import stdin

N, R = map(int, stdin.readline().split())
tree = [[] for _ in range(N + 1)]
distance = {}

for _ in range(N - 1):
    a, b, d = map(int, stdin.readline().split())
    tree[a].append(b)           # 연결된 노드 저장
    tree[b].append(a)
    distance[(a, b)] = d        # 간선 길이 저장
    distance[(b, a)] = d

print(tree)
print(distance)

pole_dist = 0
def getPoleDist(n):
    global pole_dist
    
    if len(tree[n]) > 2:     # 기가 노드는 연결된 노드가 
        return
    
    print(n)
    print(tree[n])
    print(tree[n][0])
    
    pole_dist += distance[(n, tree[n][0])]
    getPoleDist(tree[n][0])
    
    print('---')

getPoleDist(R)                  # 루트 노드부터 기둥의 길이 찾음

print(pole_dist)