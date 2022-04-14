from sys import stdin
import sys
sys.setrecursionlimit(int(10**9))

def recur(idx, preorder, inorder, subroot):
    num = preorder[idx]
    sub_idx = subroot.index(num)
    left = subroot[:sub_idx]
    right = subroot[sub_idx+1:]
    if len(left):
        remove_num = recur(idx+1, preorder, inorder, left)
        left.remove(remove_num)
        idx += 1
    if len(right):
        remove_num = recur(idx+1, preorder, inorder, right)
        right.remove(num)
    if not left and not right:
        print(num, end=" ")
        return num

T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    preorder = list(map(int, stdin.readline().split()))
    inorder = list(map(int, stdin.readline().split()))
    result = recur(0, preorder, inorder, inorder)