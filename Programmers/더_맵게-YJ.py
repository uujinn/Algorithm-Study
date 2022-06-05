import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        mixed_scovile = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, mixed_scovile)
        answer += 1

        if len(scoville) == 1 and scoville[0] < K:  # 불가능
            return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
