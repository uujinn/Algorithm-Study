from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

n = int(stdin.readline())
in_order = list(map(int, stdin.readline().split()))  # 중
post_order = list(map(int, stdin.readline().split()))  # 후


def pre(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return

    # 후위 순위 end = 서브 트리 루트
    parents = post_order[post_end]
    print(parents, end=" ")

    left = pos[parents] - in_start
    right = in_end - pos[parents]

    # 왼쪽
    pre(in_start, in_start + left - 1, post_start, post_start + left - 1)
    # 오른쪽
    pre(in_end - right + 1, in_end, post_end - right, post_end - 1)


pos = [0 for _ in range(n + 1)]
for i in range(n):
    pos[in_order[i]] = i  # 서브 트리 루트 찾기 위해 pos 저장

pre(0, n - 1, 0, n - 1)
