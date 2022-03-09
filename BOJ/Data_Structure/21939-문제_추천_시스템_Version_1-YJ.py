from collections import defaultdict
from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline().rstrip())

max_h = [] # 최대 힙
min_h = [] # 최소 힙

solved = defaultdict(bool) # 문제 풀었는지 여부

for _ in range(N):
    p, l = map(int, stdin.readline().rstrip().split())
    heappush(max_h, (-l, -p)) # 최대 힙에 (난이도, 문제 번호) push
    heappush(min_h, (l, p)) # 최소 힙에 (난이도, 문제 번호) push
    solved[p] = False 

M = int(stdin.readline().rstrip()) 

for _ in range(M):
    command = stdin.readline().split()

    if command[0] == "recommend": # 문제 번호 한 줄씩 출력해야함
        if command[1] == "1":
            while solved[-max_h[0][1]]: # 이미 푼 문제들(True) 제낌
                heappop(max_h)
            print(-max_h[0][1])

        elif command[1] == "-1":
            while solved[min_h[0][1]]: # 이미 푼 문제들(True) 제낌
                heappop(min_h)
            print(min_h[0][1])

    elif command[0] == "add":
        p = int(command[1])
        l = int(command[2])
        
        while solved[-max_h[0][1]]: # 정리
            heappop(max_h)
        while solved[min_h[0][1]]: # 정리
            heappop(min_h)

        heappush(max_h, (-l, -p))
        heappush(min_h, (l, p))
        solved[p] = False

    elif command[0] == "solved":
        p = int(command[1])
        solved[p] = True 


