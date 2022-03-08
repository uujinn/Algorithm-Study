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
            
        elif cmd == 'D':
            if val == -1 and min_heap:             # 최소값 제거
                deleted[min_heap[0][1]] = True
                heappop(min_heap)
                
            elif val == 1 and max_heap:            # 최대값 제거
                deleted[max_heap[0][1]] = True
                heappop(max_heap)
                    
        while min_heap and deleted[min_heap[0][1]]:
            heappop(min_heap)
        while max_heap and deleted[max_heap[0][1]]:
            heappop(max_heap)
        
    if not min_heap or not max_heap:
        answer += 'EMPTY\n'
    else:
        answer += (str(-max_heap[0][0]) + ' ' + str(min_heap[0][0]) + '\n')
print(answer.rstrip())