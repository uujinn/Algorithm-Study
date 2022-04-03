import sys
sys.setrecursionlimit(10**5)

tree = []
while True:
    try:
        num = int(input())
        tree.append(num)
    except:
        break

# 재귀


def preTopost(l, r):

    # 범위 벗어남
    if l > r:
        return

    root = tree[l]  # 루트
    divide = l + 1  # 나눌 위치

    for i in range(l+1, r+1):
        if tree[l] < tree[i]:
            divide = i
            break

    # 왼쪽, 오른쪽 순서대로 탐색
    preTopost(l+1, divide-1)
    preTopost(divide, r)
    print(tree[l])


preTopost(0, len(tree)-1)
