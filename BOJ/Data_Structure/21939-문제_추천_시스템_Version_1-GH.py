import sys
from heapq import heappop, heappush
from collections import defaultdict

input = sys.stdin.read()
N = int(input())

min_hq = []
max_hq = []
list = defaultdict(bool)

for _ in range(N):
    a, b = map(int, input().split())
    heappush(min_hq, [a, b])
    heappush(max_hq, [-a, -b])
    list[a] = True

M = int(input())

for _ in range(M):
    command = input().split()

    if command[0] == 'recommend':
        if command[1] == '1':
            # 조건... list[-max_hq[0][1]]을 다루면 될 것 같은뎅
            # heappop(max_hq)
        else:
            # list[min_hq[0][1]]에서 heappop(min_hq)
    elif command[0] == 'solved':
        list[int(command[1])] = False

    else:
        # 다른 난이도인데 문제 번호 같은 경우
        # 어.. 모르겟다.
