from sys import stdin
from heapq import heappush, heappop

answer = ''
for _ in range(int(stdin.readline())):          # T번 반복
    min_heap = []                               # 최솟값 출력 위한 heap
    max_heap = []                               # 최댓값 출력 위한 heap
    deleted = {}
    
    for i in range(int(stdin.readline())):      # K번 반복
        cmd, val = stdin.readline().split()
        val = int(val)

        if cmd == 'I':
            heappush(min_heap, (val, i))
            heappush(max_heap, (-val, i))
            deleted[i] = False
            
        elif min_heap and max_heap and cmd == 'D':
            if val == -1 and min_heap:             # 최소값 제거
                min_val = heappop(min_heap)[1]
                deleted[min_val] = True
                
            elif val == 1 and max_heap:            # 최대값 제거
                max_val = -heappop(max_heap)[1]
                deleted[max_val] = True
                    
        while min_heap and deleted[min_heap[0][1]]:
            # print(heappop(min_heap))
            heappop(min_heap)
        while max_heap and deleted[max_heap[0][1]]:
            # print(heappop(max_heap))
            heappop(max_heap)
                    
        # print('min heap : ', end='')
        # print(min_heap)
        # print('max heap : ', end='')
        # print(max_heap)
        # print('deleted : ', end='')
        # print(deleted)
        # print('-------------')
        
    if not min_heap or not max_heap:
        answer += 'EMPTY\n'
    else:
        answer += (str(-max_heap[0][0]) + ' ' + str(min_heap[0][0]) + '\n')
        
print(answer.rstrip())