import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while True:
        if scoville[0] < K:
            t = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
            heapq.heappush(scoville, t)
            answer += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

        if scoville[0] >= K:
            return answer