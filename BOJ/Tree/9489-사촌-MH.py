from sys import stdin

while True:
    n, k = map(int, stdin.readline().split())
    
    if n == 0:
        break
    
    tree = [[] for _ in range(n)]
    nodes = list(map(int, stdin.readline().split()))
    # nodes : [1, 3, 4, 5, 8, 9, 15, 30, 31, 32]
    print(nodes)
    print(tree)
    
    depth = 0
    for n in nodes:
        if len(tree[0]) == 0:       # root에 값이 들어가면 depth 추가
            tree[depth].append([n])
            depth += 1
        else:
            print('n : ', end='')
            print(n, end=', ')
            
            if tree[depth] and tree[depth][-1][-1] + 1 != n:
                print(tree[depth][-1][-1] + 1)
                depth += 1
                tree[depth].append([n])
            else:
                tree[depth].append([n])
            
        
        print(tree)