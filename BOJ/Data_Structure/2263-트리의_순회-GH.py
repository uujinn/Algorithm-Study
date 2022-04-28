import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
position = [0] * (n+1)

for i in range(n):
    position[inOrder[i]] = i


def preOrder(iStart, iEnd, pStart, pEnd):
    if iStart > iEnd or pStart > pEnd:
        return

    root = postOrder[pEnd]
    print(root, end=' ')

    left = position[root] - iStart
    right = iEnd - position[root]

    preOrder(iStart, position[root]-1, pStart, pStart+left-1)
    preOrder(position[root]+1, iEnd, pEnd-right, pEnd-1)


preOrder(0, n-1, 0, n-1)