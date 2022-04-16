from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def postorder(left, right, cur):
    for i in range(left, right + 1):
        if pre_arr[cur] == in_arr[i]:                       # 전위순회로 root 찾음
            postorder(left, i - 1, cur + 1)                 # 왼쪽 서브트리
            postorder(i + 1, right, cur + i - left + 1)     # 오른쪽 서브트리
            print(pre_arr[cur], end=' ')
    
T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    pre_arr = list(map(int, stdin.readline().split()))      # 전위순회 (preorder)
    in_arr = list(map(int, stdin.readline().split()))       # 중위순회 (inorder)
    
    postorder(0, n - 1, 0)
    print()