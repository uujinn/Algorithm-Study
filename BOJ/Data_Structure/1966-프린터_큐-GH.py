from collections import deque
from sys import stdin

num = int(stdin.readline())

for _ in range(num):
    # 문서의 개수 = N, 인쇄된 순서가 궁금한 문서의 현재 큐의 위치 = M
    N, M = map(int,stdin.readline().split())
    queue = deque(map(int,stdin.readline().split()))
    cnt = 0
    
    while queue:
        top = max(queue)
        M -= 1
        
        # queue의 가장 앞을 빼서 그 숫자가 가장 큰 숫자인지 확인
        pop = queue.popleft()
        if top != pop:
            queue.append(pop)
            if M < 0:
                M = len(queue)-1
                
        # 가장 큰 숫자이면 빠진 상태로 두고 빠진 숫자의 개수를 하나씩 셈
        else:
            cnt += 1
            if M == -1:
                # 원하는 숫자가 빠져 나갔을 때, 몇 번째로 빠져 나갔는지 숫자 출력
                print(cnt)
                break