from sys import stdin
case = 1
lines = []
temp = ""
while True:
    temp += stdin.readline().rstrip()
    if temp[-5:] == '-1 -1': 
        lines.append(temp[:-5])
        break
    elif temp[-1] == " ": 
        lines.append(temp)
        temp = ""
    else: temp += "  "

for line in lines:
    u_vs = list(map(str, line.split("  ")))
    tree = {}
    v_flag = {}
    result = True
    
    for u_v in u_vs[:-1]:
        u, v = u_v.split()
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
    
    if u_vs[0] == '0 0': result = True
    
    if not result: print("Case %d is not a tree." % case)
    else: print("Case %d is a tree." % case)
    case += 1