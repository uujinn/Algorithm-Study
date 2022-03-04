from sys import stdin
import heapq
N = int(stdin.readline())
heap = []
for _ in range(N):
    tmp = list(map(int, stdin.readline().split()))
    for t in tmp:
        if len(heap) == N: #꽉 차 있을때
            if t > heap[0]: heapq.heappushpop(heap, t) #무조건 제일 큰 수부터 N번째 큰 수만 힙 안에 들어가 있을 수 있도록 크기 유지
        else:
            heapq.heappush(heap, t)
            
print(heap[0]) #마지막에는 가장 작은 숫자가 결국 N번째 큰 수임