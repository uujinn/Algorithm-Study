from sys import stdin

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def pre_order(node): #전위순회
    if node is not None:
        print(node.data, end='')
        pre_order(node.left_child)
        pre_order(node.right_child)
    
def in_order(node): #중위순회
    if node is not None:
        in_order(node.left_child)
        print(node.data, end='')
        in_order(node.right_child)

def post_order(node): #후위순회
    if node is not None:
        post_order(node.left_child)
        post_order(node.right_child)
        print(node.data, end='')

N = int(stdin.readline())
tree = [0] * 26
for _ in range(N):
    parent, left_c, right_c = map(str, stdin.readline().split())
    if _ == 0: tree[0] = Node(parent)
    if left_c != '.': 
        tree[ord(left_c)-65] = Node(left_c)
        tree[ord(parent)-65].left_child = tree[ord(left_c)-65]
    if right_c != '.': 
        tree[ord(right_c)-65] = Node(right_c)
        tree[ord(parent)-65].right_child = tree[ord(right_c)-65]

pre_order(tree[0])
print()
in_order(tree[0])
print()
post_order(tree[0])