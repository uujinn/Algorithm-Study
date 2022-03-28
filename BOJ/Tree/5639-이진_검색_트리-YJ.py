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

    root = tree[l] # 루트
    idx = l + 1 # 왼쪽 서브트리

    # 서브트리 끝까지 검색
    while idx <= r:
        # 루트보다 크면 오른쪽 서브트리임 ex. 98
        if root < tree[idx]:
            break # 오른쪽 찾았으니깐 멈춤
        idx += 1

    # 왼쪽, 오른쪽 순서대로 탐색
    preTopost(l+1, idx-1)
    preTopost(idx, r)
    print(root)


preTopost(0, len(tree)-1)