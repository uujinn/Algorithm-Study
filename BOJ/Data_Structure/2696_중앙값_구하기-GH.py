import sys
import heapq

def isCheck(data):
    l, r = [], []
    center = data[0]
    result = [center]

    for idx, val in enumerate(data[1: ], 1):
        if val > middle:
            heapq.heappush(r, val)
        else:
            heapq.heappush(l, -val)
        if idx % 2 == 0:
            if len(l) < len(r):
                heapq.heappush(l, -middle)
                middle = heapq.heappop(r)

            elif len(l) > len(r):
                heapq.heappush(r, middle)
                middle = -heapq.heappop(l)
            result.append(middle)

    print(len(result))

# ???????????
# 엥 for문 하나 더 만들어야 된다
# 제가 오늘... 시간이 없어서 다 못 짰습니다...
# 사과드립니다... 주말에 멋진 코드 들고 올게요.. ..