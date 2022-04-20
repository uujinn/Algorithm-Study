from sys import stdin

# 1. 단 하나의 root가 존재, 즉 부모가 없는 노드는 하나
# 2. root를 제외한 모든 노드는 들어오는 간선이 하나여야 함
# 3. root에서 다른 노드로 가는 경로는 유일함 (정점의 개수 - 1 == 간선의 수)
# 4. 비어있어도 tree

def isTree(temp):                   # 입력받은 값으로 간선 이은 list 생성
    vertices = []
    link_count = 0
    tree = [[] for _ in range(max(temp) + 1)]

    for i in range(0, len(temp) - 3, 2):    # 0 0 값 제외하고 리스트에 추가
        vertices.append(temp[i])
        vertices.append(temp[i + 1])
        link_count += 1
        tree[temp[i]].append(temp[i + 1])
        
    # [[], [], [], [], [], [3, 2, 6], [8, 4], [], [], [], [], []]
    # 5에서 나간 간선이 3, 2, 6으로 들어감
    # 6에서 나간 간선이 8, 4로 들어감
    
    vertices = set(vertices)
    
    if (len(vertices) == 0):
        return True
    elif (len(vertices) - 1 == link_count):
        return True
    else:
        return False


case_count = 1
trees = [[] for _ in range(2)]       # 안 쓰는 0번째 칸과 값을 채울 1번째 칸 생성

while True:
    temp = list(map(int, stdin.readline().split()))
    trees[case_count].extend(temp)
    
    if 0 in temp:               # 0 0 입력 시 테스트 케이스 끝
        if isTree(trees[case_count]):
            print('Case ' + str(case_count) + ' is a tree.')
        else:
            print('Case ' + str(case_count) + ' is not a tree.')
            
        # visited = [False for _ in range(max(trees[case_count]) + 1)]        # len - 2
        
        case_count += 1
        trees.append([])
    elif -1 in temp:            # -1 -1 입력 시 
        break
# trees : [[], [6, 8, 5, 3, 5, 2, 6, 4, 5, 6, 0, 0], [5, 3, 5, 6, 5, 2, 0, 0], [-1, -1]]