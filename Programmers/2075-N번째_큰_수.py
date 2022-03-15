from sys import stdin
from heapq import heappop, heappush

heap = []                   # 길이 N을 유지하는 최소 힙
N = int(stdin.readline())

for _ in range(N):
    nums = list(map(int, stdin.readline().split()))
    
    if not heap:            # heap에 값이 없으면 입력받은 5개 값 모두 넣어줌
        for num in nums:
            heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num:
                heappop(heap)           # heap의 최소값 제거
                heappush(heap, num)

print(heap[0])              # 길이 N인 힙에서 최소값 추출 (N번째로 큰 수)