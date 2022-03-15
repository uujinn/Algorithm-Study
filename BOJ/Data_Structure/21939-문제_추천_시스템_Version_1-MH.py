from sys import stdin
from heapq import heappush, heappop

min_heap = []                   # 가장 쉬운 문제의 번호 출력 위함
max_heap = []                   # 가장 어려운 문제의 번호 출력 위함
solved = {}                     # 문제가 풀렸으면 0, 풀리지 않았으면 문제의 레벨

for i in range(int(stdin.readline())):
    P, L = map(int, stdin.readline().split())
    heappush(min_heap, (L, P))
    heappush(max_heap, (-L, -P))
    solved[P] = L               # 현재 P의 L 저장
    
for _ in range(int(stdin.readline())):
    cmd = list(stdin.readline().split())
    cmd[1] = int(cmd[1])
    
    if cmd[0] == 'recommend':
        if cmd[1] == 1:
            while solved[-max_heap[0][1]] != -max_heap[0][0]:
                heappop(max_heap)
            print(-max_heap[0][1])
            
        elif cmd[1] == -1:
            while solved[min_heap[0][1]] != min_heap[0][0]:
                heappop(min_heap)
            print(min_heap[0][1])
    
    elif cmd[0] == 'add':
        cmd[2] = int(cmd[2])
        
        while solved[-max_heap[0][1]] != -max_heap[0][0]:       # 같은 번호 다른 난이도 문제 방지
            heappop(max_heap)
        while solved[min_heap[0][1]] != min_heap[0][0]:
            heappop(min_heap)
            
        heappush(min_heap, (cmd[2], cmd[1]))
        heappush(max_heap, (-cmd[2], -cmd[1]))
        solved[cmd[1]] = cmd[2]
    
    elif cmd[0] == 'solved':
        solved[cmd[1]] = 0      # 풀린 문제는 L을 0으로 설정