from sys import stdin
import sys
sys.setrecursionlimit(int(10**9))

def recur(left, right, root):
    if left > right: 
        return
    if left == right:
        print(preorder[root], end=" ")
        return
    idx = inorder.index(preorder[root])
    recur(left, idx-1, root+1)
    recur(idx+1, right, (idx-left)+root+1)
    print(preorder[root], end=" ")

T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    preorder = list(map(int, stdin.readline().split()))
    inorder = list(map(int, stdin.readline().split()))
    recur(0, n-1, 0)
    print()