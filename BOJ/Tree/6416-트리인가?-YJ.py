from collections import deque
from sys import stdin

# 인풋을 전부 다 받고 시행
all_input = []
while True:
    try:
        # 줄마다 끊어서 input
        tmp = list(map(int, stdin.readline().rstrip().split()))
        # print(tmp)
        if tmp == [-1, -1]:
            break
        all_input.append(tmp)
    except:
        break

# print(all_input)

cases = []  # case1, 2, 3
case_part = []  # ex. case1 - (6, 8) (5, 3) (5, 2) (6, 4) // (5, 6)

for line in all_input:  # 한 줄 마다 check
    # 줄 마지막이 [0, 0]이면 case_part에 그 앞 (u, v) 넣어주고 다음 case로 넘어감
    if line[-2:] == [0, 0]:
        case_part += line[:-2]
        cases.append(case_part)
        case_part = []
    else:  # 아니라면 전체 다 case_part에 추가
        case_part += line


# print(cases)

for case in range(len(cases)):
    edges = cases[case]
    # print(edges)

    # 트리 생성
    parent = dict()
    child = dict()
    nodes = set()  # 중복 없이 모든 노드

    for i in range(len(edges) // 2):
        # (6, 8) (5, 3) (5, 2) (6, 4), (5, 6)
        u, v = edges[i * 2], edges[i * 2 + 1]  # 여기서 (u, v) 뽑음
        # print(u, v)
        nodes.update((u, v))
        if u in child:  # u의 자식 노드들
            child[u].append(v)
        else:  # 없으면 새로 등록
            child[u] = [v]
        if v in parent:  # v의 부모노드들
            parent[v].append(u)
        else:  # 없으면 새로 등록
            parent[v] = [u]

    # print(parent)
    # print(child)
    # 루트는 들어오는 간선이 존재하면 안됨 부모 dict 키에 있으면 안됨 -> 차집합
    root = list(nodes - set(parent.keys()))

    if len(root) != 1:  # 루트 여러개면 트리 아님
        print(f'Case {case + 1} is not a tree.')

    else:  # 그리고 또.. 들어오는 간선이 여러개면 안됨..
        for v in parent.values():
            if len(v) > 1:
                print(f'Case {case + 1} is not a tree.')
                break
            else:
                print(f'Case {case + 1} is a tree.')
                break

    