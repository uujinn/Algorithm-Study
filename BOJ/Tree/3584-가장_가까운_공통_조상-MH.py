from sys import stdin

def get_parent(A, B):
    global nodes
    A_parents, B_parents = [], []
    
    next = A                            # A의 모든 부모 저장
    A_parents.append(next)
    while True:
        if nodes[next] == -1:
            break
        A_parents.append(nodes[next])
        next = nodes[next]
    
    next = B                            # B의 모든 부모 저장
    B_parents.append(next)
    while True:
        if nodes[next] == -1:
            break
        B_parents.append(nodes[next])
        next = nodes[next]
        
    for A_parent in A_parents:          # 저장된 부모들 비교
        for B_parent in B_parents:
            if A_parent == B_parent:
                return A_parent
    return A_parent[-1]                 # 공통된 부모가 없으면 root 반환
    
    
for _ in range(int(stdin.readline())):          # T개의 테스트 케이스
    N = int(stdin.readline())
    nodes = [-1 for _ in range(N + 1)]
    
    for _ in range(N - 1):
        parent, child = map(int, stdin.readline().split())
        nodes[child] = parent
        
    A, B = map(int, stdin.readline().split())   # 공통 조상을 구할 두 노드
    print(get_parent(A, B))