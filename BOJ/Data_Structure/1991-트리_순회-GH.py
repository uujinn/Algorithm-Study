import sys

n = int(sys.stdin.readline())
tree = dict()

for i in range(n):
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = left, right

def pre(v):
    if v != ".":
        print(v, end="")
        pre(tree[v][0])
        pre(tree[v][1])

def center(v):
    if v != ".":
        center(tree[v][0])
        print(v, end="")
        center(tree[v][1])

def post(v):
    if v != ".":
        post(tree[v][0])
        post(tree[v][1])
        print(v, end="")


pre('A')
print()
center('A')
print()
post('A')