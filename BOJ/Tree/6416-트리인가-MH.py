from sys import stdin

def makeTree(temp):                   # 입력받은 값으로 간선 이은 list 생성
    tree = [[] for _ in range(len(temp))]

    for i in range(0, len(temp) - 3, 2):    # 0 0 값 제외하고 리스트에 추가
        tree[temp[i]].append(temp[i + 1])
        
    # [[], [], [], [], [], [3, 2, 6], [8, 4], [], [], [], [], []]
    # 5에서 나간 간선이 3, 2, 6으로 들어감
    # 6에서 나간 간선이 8, 4로 들어감
    return tree


def isTree(tree):                    # 이어진 간선 list를 받아 tree인지 판별
    global visited
    
    print(tree)
    print(visited)
    
    # for nodes in tree:      
    #     for node in nodes:
    #         print(node)
    
    
    return 0


case_count = 1
trees = [[] for _ in range(2)]       # 안 쓰는 0번째 칸과 값을 채울 1번째 칸 생성

while True:
    temp = list(map(int, stdin.readline().split()))
    trees[case_count].extend(temp)
    
    if 0 in temp:               # 0 0 입력 시 테스트 케이스 끝
        tree = makeTree(trees[case_count])
        visited = [False for _ in range(max(trees[case_count]) + 1)]        # len - 2
        isTree(tree)
        
        case_count += 1
        trees.append([])
        
    elif -1 in temp:            # -1 -1 입력 시 
        break
# [[], [6, 8, 5, 3, 5, 2, 6, 4, 5, 6, 0, 0], [5, 3, 5, 6, 5, 2, 0, 0], [-1, -1]]