from sys import stdin
from collections import deque

def printer_queue():
    N, M = map(int, stdin.readline().rstrip().split())            # 문서의 개수 N, 궁금한 문서의 위치 M
    que = deque(map(int, stdin.readline().rstrip().split()))      # N개의 중요도 입력받음

    cnt = 0
    while que:
        if que[0] < max(que):
            que.rotate(-1)
        else:
            if M == 0:
                return cnt + 1 

            que.popleft()
            cnt += 1
        M = M - 1 if M > 0 else len(que) - 1

    return cnt + 1


case_num = int(stdin.readline())
for i in range(case_num):
    print(printer_queue())

# 92ms