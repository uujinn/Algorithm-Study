from dataclasses import dataclass
from sys import stdin

def Preorder(root):     # 전위 순회 : root -> left -> right
    if root != '.':
        print(root, end='')
        Preorder(tree[root][0])
        Preorder(tree[root][1])

def Inorder(root):      # 중위 순회 : left -> root -> right
    if root != '.':
        Inorder(tree[root][0])
        print(root, end='')
        Inorder(tree[root][1])

def Postorder(root):    # 후위 순회 : left -> right -> root
    if root != '.':
        Postorder(tree[root][0])
        Postorder(tree[root][1])
        print(root, end='')

tree = {}
N = int(stdin.readline())

for i in range(N):
    data, left, right = stdin.readline().rstrip().split()    
    tree[data] = (left, right)
    
Preorder('A')
print()
Inorder('A')
print()
Postorder('A')