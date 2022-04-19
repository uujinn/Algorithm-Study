import sys

sys.setrecursionlimit(10 ** 6)
num_list = []

while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break


def postOrder(first, end):
    if first > end:
        return
    mid = end + 1
    # 루트보다 크지 않을 때
    for i in range(first+1, end+1):
        if num_list[first] < num_list[i]:
            mid = i
            break

    postOrder(first+1, mid-1)
    postOrder(mid, end)
    print(num_list[first])

postOrder(0, len(num_list)-1)