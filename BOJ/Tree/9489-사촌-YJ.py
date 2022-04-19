from sys import stdin

while True:
    n, k = map(int, stdin.readline().rstrip().split())
    if n == k == 0:
        break

    nodes = [-1]  # 인덱스 맞추기 위해 기본 노드 넣어줌
    nodes.extend(list(map(int, stdin.readline().rstrip().split())))
    depth = -1
    idx = 0
    group = [-1] * (n+1)  # 그룹으로 묶어주기

    for i in range(1, n+1):
        if nodes[i] == k:
            idx = i  # 사촌을 구해야하는 노드의 인덱스
            # print(f'idx: {idx}')
        if nodes[i] - nodes[i-1] != 1:  # 차이가 1 넘게 나면 depth 추가
            depth += 1
        group[i] = depth

    # print(group)  # [-1, 0, 1, 1, 1, 2, 2, 3, 4, 4, 4]

    c = 0
    grandparent = group[group[idx]]  # 할아버지 노드
    # print(f'grandparent: {group[group[idx]]}') # 1
    # print(f'parent: {group[idx]}') # 3
    for i in range(1, n+1):
        if group[i] != group[idx] and group[group[i]] == grandparent:
            c += 1

    print(c)
