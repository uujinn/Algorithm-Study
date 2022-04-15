from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

n = int(stdin.readline())
in_arr = list(map(int, stdin.readline().split()))       # 중위순회 (inorder)
post_arr = list(map(int, stdin.readline().split()))     # 후위순회 (postorder)

# 중위순회에서 root의 인덱스 기준으로 왼쪽 오른쪽 서브트리 구분 가능
idx = [0] * (n + 1)
for i in range(n):
    idx[in_arr[i]] = i

# 전위순회 (preorder) : root -> 왼 -> 오
def preorder(in_l, in_r, post_l, post_r):
    # 역전되면 구분할 노드가 없음
    if in_l > in_r or post_l > post_r:
        return
    
    root = post_arr[post_r]     # 후위순회의 마지막 노드는 root
    print(root, end=' ')
    
    left = idx[root] - in_l
    right = in_r - idx[root]
    
    # 전위순회이므로 root 출력 후 왼쪽 출력
    preorder(in_l, in_l + left - 1, post_l, post_l + left - 1)
    # 오른쪽 출력
    preorder(in_r - right + 1, in_r, post_r - right, post_r - 1)

preorder(0, n - 1, 0, n - 1)