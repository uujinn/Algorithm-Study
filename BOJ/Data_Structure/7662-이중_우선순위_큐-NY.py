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
                while heap_min and numbers[heap_min[0][1]]: heapq.heappop(heap_min)
                if heap_min:
                    numbers[heap_min[0][1]] = True
                    heapq.heappop(heap_min)
            else: #최대값 제거
                while heap_max and numbers[heap_max[0][1]]: heapq.heappop(heap_max)
                if heap_max:
                    numbers[heap_max[0][1]] = True
                    heapq.heappop(heap_max)
                    
    while heap_min and numbers[heap_min[0][1]]: heapq.heappop(heap_min)
    while heap_max and numbers[heap_max[0][1]]: heapq.heappop(heap_max) #만약 D -1 만 계속 나왔다면 동기화가 안되어 있을 수 있어서 마지막에 한 번 더 해줌
            
    if heap_max and heap_min: print("%d %d" %(-heap_max[0][0], heap_min[0][0]))
    else: print("EMPTY")