tree = []

while True:
    try:
        num = int(input())
        tree.append(num)
    except:
        break

# 재귀


def preTopost(l, r):
    try:
        root = pre[l]  # 루트 노드
    except:
        exit(0)

    for i, val in enumerate(pre):
        if root < val:  # 예시에서 98이 오른쪽 트리의 루트
            r = i
            # print(pre[r])
            break

    left = pre[l+1: r]
    right = pre[r: len(pre)]

    print(left)
    print(right)


pre = [50, 30, 24, 5, 28, 45, 98, 52, 60]

print(preTopost(0, 1))
