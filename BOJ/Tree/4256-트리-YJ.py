from sys import stdin
import sys

sys.setrecursionlimit(50000)


def post_order(start, end, pos):  # pos = 현재 위치
    for i in range(start, end + 1):
        if pre_arr[pos] == in_arr[i]:
            # 후위 순회 = 왼쪽 자식 -> 오른쪽 자식 -> 루트 print
            post_order(start, i - 1, pos + 1)  # 왼쪽 서브트리 재귀
            post_order(i + 1, end, pos + i - start + 1)  # 오른쪽 서브트리 재귀
            # pos 오른쪽 자식 인덱스 =  왼쪽 서브 트리 노드의 수 + 1
            print(pre_arr[pos], end=' ')  # 루트


T = int(stdin.readline().rstrip())
for _ in range(T):
    n = int(stdin.readline().rstrip())
    pre_arr = list(map(int, stdin.readline().rstrip().split()))
    in_arr = list(map(int, stdin.readline().rstrip().split()))
    post_order(0, n-1, 0)
    print()
