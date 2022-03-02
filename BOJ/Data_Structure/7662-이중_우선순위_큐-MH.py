from sys import stdin
import heapq

answer = ''

for _ in range(int(stdin.readline())):          # T번 반복
    heap = []                                   # 오름차순으로 정렬된 deque
    
    for _ in range(int(stdin.readline())):      # K번 반복
        cmd, val = stdin.readline().split()

        if cmd == 'I':
            heapq.heappush(heap, int(val))
        elif heap and cmd == 'D':
            if val == '-1':             # 최소값 제거
                heapq.heappop(heap)
            elif val == '1':            # 최대값 제거
                heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
        
        print(heap)
        
    if not heap:
        answer += 'EMPTY\n'
    else:
        answer += (str(heapq.nlargest(1, heap)[0]) + ' ' + str(heap[0]) + '\n')

    print('-----')

print(answer)