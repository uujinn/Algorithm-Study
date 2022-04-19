from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def makeBinaryTree(tree, seq, level):
    mid = len(seq) // 2
    tree[level].append(seq[mid])
    
    if len(seq) == 1:
        return
    
    makeBinaryTree(tree, seq[:mid], level + 1)
    makeBinaryTree(tree, seq[mid + 1:], level + 1)
    

K = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))
tree = [[] for _ in range(K)]

makeBinaryTree(tree, seq, 0)

for i in range(len(tree)):
    [print(j, end=' ') for j in tree[i]]
    print()