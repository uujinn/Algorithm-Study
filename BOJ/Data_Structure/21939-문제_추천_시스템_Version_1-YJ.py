from collections import defaultdict
from sys import stdin
from heapq import heappop, heappush
from xmlrpc.client import Boolean

N = int(stdin.readline().rstrip())

max_h = [] # 최대 힙
min_h = [] # 최소 힙

solved = defaultdict(Boolean) # 문제 풀었는지 여부

for _ in range(N):
    p, l = map(int, stdin.readline().rstrip().split())
    heappush(max_h, (-l, p)) # 최대 힙에 (난이도, 문제 번호) push
    heappush(min_h, (l, p)) # 최소 힙에 (난이도, 문제 번호) push
    solved[p] = False 

M = int(stdin.readline().rstrip()) 

for _ in range(M):
    command = stdin.readline().split()

    if command[0] == "recommend": # 문제 번호 한 줄씩 출력해야함
        if command[1] == 1:
            # 이 부분 ................ 문제 있는듯
            while max_h and solved[max_h[0][1]]:
                print(max_h[0][1])
                break

        elif command[1] == -1:
            # 이 부분 ................ 문제 있는듯
            while min_h and solved[min_h[0][1]]:
                print(min_h[0][1])
                break

    elif command[0] == "add":
        p = int(command[1])
        l = int(command[2])
        heappush(max_h, (-l, p))
        heappush(min_h, (l, p))
        solved[p] = False

    elif command[0] == "solved":
        p = int(command[1])
        solved[p] = True # 문제 풀었음
        # 여기도.......... 문제 있는듯

