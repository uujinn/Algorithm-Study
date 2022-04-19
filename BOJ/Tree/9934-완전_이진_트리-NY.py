import sys
sys.setrecursionlimit(int(100000))

K = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(K)]

def make_tree(arr, depth):
    parent = len(arr)//2
    tree[depth].append(arr[parent]) #해당 깊이의 배열에 중간값 저장
    if len(arr) == 1:
        return
    else: #재귀
        make_tree(arr[:parent], depth+1)
        make_tree(arr[parent+1:], depth+1)

make_tree(nodes, 0)

for same_depth in tree:
    for num in same_depth:
        print(num, end=" ")
    print()