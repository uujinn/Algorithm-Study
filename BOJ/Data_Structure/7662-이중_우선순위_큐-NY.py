from sys import stdin
import heapq
T = int(stdin.readline())
for _ in range(T):
    heap_max = []
    heap_min = []
    k = int(stdin.readline())
    numbers = [False] * k
    for i in range(k):
        letter, num = map(str, stdin.readline().split())
        num = int(num)
        if letter=="I":
            heapq.heappush(heap_max, (-num, i))
            heapq.heappush(heap_min, (num, i))
        elif letter=="D" and heap_max and heap_min: #비어 있지 않을때
            if num == -1: #최소값 제거
                numbers[heap_min[0][1]] = True
                heapq.heappop(heap_min)
            else: #최대값 제거
                numbers[heap_max[0][1]] = True
                heapq.heappop(heap_max)
            
            for j in heap_min:
                if numbers[j[1]]: heapq.heappop(heap_min)
                else: heapq.heappushpop(heap_min, j)
            for j in heap_max:
                if numbers[j[1]]: heapq.heappop(heap_max)
                else: heapq.heappushpop(heap_max, j)
            
    if heap_max and heap_min: print("%d %d" %(-heap_max[0][0], heap_min[0][0]))
    else: print("EMPTY")