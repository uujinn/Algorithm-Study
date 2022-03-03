from sys import stdin
import heapq
T = int(stdin.readline())
for _ in range(T):
    heap = []
    k = int(stdin.readline())
    for _ in range(k):
        letter, num = map(str, stdin.readline().split())
        if letter=="I":
            heapq.heappush(heap, int(num))
        elif letter=="D" and heap: #비어 있지 않을때
            if int(num) == -1: #최소값 제거
                heapq.heapify(heap)
                heapq.heappop(heap) 
            else: #최대값 제거
                heapq._heapify_max(heap)
                heapq.heappop(heap)
    if heap: print("%d %d" %(max(heap), min(heap)))
    else: print("EMPTY")