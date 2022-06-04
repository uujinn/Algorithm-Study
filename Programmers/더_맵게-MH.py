from heapq import heappop, heappush, heapify

def solution(scoville, K):
    heapify(scoville)
    count = 0
    
    while scoville[0] < K and len(scoville) >= 2:
        temp = heappop(scoville) + heappop(scoville) * 2
        heappush(scoville, temp)
        count += 1
        
    return count if scoville[0] >= K else -1

print(solution([2, 1, 3, 9, 10, 12], 7))