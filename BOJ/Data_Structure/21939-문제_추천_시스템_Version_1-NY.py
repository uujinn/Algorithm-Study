from sys import stdin
import heapq

N = int(stdin.readline())
max_heap = []
min_heap = []
solved = {}
for _ in range(N):
    P, L = map(int, stdin.readline().split())
    heapq.heappush(max_heap, (-L, P))
    heapq.heappush(min_heap, (L, P))
    solved[P] = False
M = int(stdin.readline())
for _ in range(M):
    s = list(stdin.readline().split())
    if s[0] == "recommend":
        if s[1] == "1":
            while max_heap and solved[max_heap[0][1]]: heapq.heappop(max_heap)
            if max_heap: print(max_heap[0][1])
        else:
            while min_heap and solved[min_heap[0][1]]: heapq.heappop(min_heap)
            if min_heap: print(min_heap[0][1])
    elif s[0] == "add":
        heapq.heappush(max_heap, (-int(s[2]), int(s[1])))
        heapq.heappush(min_heap, (int(s[2]), int(s[1])))
        solved[int(s[1])] = False
    elif s[0] == "solved":
        solved[int(s[1])] = True
        while max_heap and solved[max_heap[0][1]]: heapq.heappop(max_heap)
        while min_heap and solved[min_heap[0][1]]: heapq.heappop(min_heap)