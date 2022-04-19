from sys import stdin

N = int(stdin.readline())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
    
q = int(stdin.readline())
for _ in range(q):
    t, k = map(int, stdin.readline().split())
    
    if t == 1:                                  # 단절점인지 판별
        print('no') if len(tree[k]) < 2 else print('yes')
    elif t == 2:                                # 단절선인지 판별
        print('yes')                            # 모든 선은 단절선