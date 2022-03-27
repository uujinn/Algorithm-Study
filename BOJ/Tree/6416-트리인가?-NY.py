from sys import stdin
case = 1
while True:
    temp = []
    tree = {}
    v_flag = {}
    result = True
    while True:
        temp += list(map(str, stdin.readline().rstrip().split("  ")))
        if temp[-1] == '0 0': continue
        elif temp[-2] == '0 0': break
    
    for t in temp[:-1]:
        u, v = t.split()
        if v in v_flag: #이미 다른 u에서 v로 들어오는 간선이 있는데 또 새로 들어갈 경우
            result = False
            break
        if u not in tree: tree[u] = [v]
        else: tree[u].append(v)
        v_flag[v] = True
    
    if result: #루트 노드가 있는지 검사
        result = False
        for key in tree:
            if key not in v_flag: 
                result = True
    
    if temp[0] == '0 0': result = True
    
    if not result: print("Case %d is not a tree." % case)
    else: print("Case %d is a tree." % case)
    case += 1
    
    if temp[-1] != '': exit(0)