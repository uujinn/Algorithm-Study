from sys import stdin
tree = []

def sol(start, end):
    if start > end:
        return

    div = end + 1

    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            div = i
            break

    sol(start + 1, div - 1)
    sol(div, end)
    print(tree[start])

while True:
    try:
        n = int(stdin.readline())
    except:
        break
    tree.append(n)

sol(0, len(tree)-1)

