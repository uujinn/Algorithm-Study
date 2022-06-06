from sys import stdin

while True:
    n, k = map(int, stdin.readline().split())
    
    if n == 0:
        break
    
    nodes = [-1]        # 인덱스 맞추기 위함
    nodes.extend(list(map(int, stdin.readline().split())))
    # nodes : [1, 3, 4, 5, 8, 9, 15, 30, 31, 32]
    print(nodes)
    
    depth = 0
    # 할아버지 노드가 같은 손자 노드들을 찾아서 훑기 but 부모 노드가 같으면 안됨
    