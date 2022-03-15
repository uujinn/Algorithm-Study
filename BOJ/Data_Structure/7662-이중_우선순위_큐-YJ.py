from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict

for i in range(int(stdin.readline())): # T
    min_h = [] # 최소 힙
    max_h = [] # 최대 힙

    counts = defaultdict(int) # Counter 역할
    for i in range(int(stdin.readline())): # K
        command, n = map(str, stdin.readline().rstrip().split())
        if command == "I":
            counts[int(n)] += 1

            heappush(min_h, int(n))
            heappush(max_h, -int(n)) # 최대 힙은 음수로 넣어줌
        
        elif command == "D":
            if n == "1": # Q에서 최댓값을 삭제하는 연산
                while max_h:
                    tmp = -heappop(max_h) # 최대힙 사용했으므로 음수 붙여줌
                    if counts.get(tmp):
                        counts[tmp] -= 1
                        break

            elif n == "-1": # Q에서 최솟값을 삭제하는 연산
                while min_h:
                    tmp = heappop(min_h)
                    if counts.get(tmp):
                        counts[tmp] -= 1
                        break
    
    answer = [key for key, value in counts.items() if value > 0]
    if answer:
        answer.sort()
        print(answer[-1], answer[0])
    else:
        print("EMPTY")