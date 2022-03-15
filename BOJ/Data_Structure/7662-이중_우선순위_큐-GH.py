import sys
import heapq

T = int(input())

for _ in range(T):

    k = int(input())
    max_hq = []
    min_hq = []
    delete_check = [0] * k  # 삭제됐는지 체크

    for i in range(k):
        a, b = sys.stdin.readline().split()

        if a == 'I':
            heapq.heappush(max_hq, ((-1) * int(b), i))
            heapq.heappush(min_hq, (int(b), i))

        elif a == 'D':
            if b == '-1':  # min
                while min_hq:
                    if delete_check[min_hq[0][1]] == 1:
                        heapq.heappop(min_hq)
                    else:
                        break
                if min_hq:
                    min = min_hq[0][1]
                    delete_check[min] = 1
                    heapq.heappop(min_hq)

            elif b == '1':
                while max_hq:
                    if delete_check[max_hq[0][1]] == 1:
                        heapq.heappop(max_hq)
                    else:
                        break
                if max_hq:
                    max = max_hq[0][1]
                    delete_check[max] = 1
                    heapq.heappop(max_hq)

    while max_hq:
        if delete_check[max_hq[0][1]] == 1:
            heapq.heappop(max_hq)
        else:
            break

    while min_hq:
        if delete_check[min_hq[0][1]] == 1:
            heapq.heappop(min_hq)
        else:
            break

    if min_hq:
        print((-1) * max_hq[0][0], min_hq[0][0])
    else:
        print("EMPTY")