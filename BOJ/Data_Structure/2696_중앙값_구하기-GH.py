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

    for i in range(len(result)):
        if (i + 1) != 1 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m = int(input())
    data = []

    if m % 10 == 0:
        for _ in range(m // 10):
            data.extend(list(map(int, sys.stdin.readline().rstrip().split())))
    else:
        for _ in range(m // 10 + 1):
            data.extend(list(map(int, sys.stdin.readline().rstrip().split())))

    isCheck(data)