from sys import stdin
from heapq import heappush, heappop

min_heap = []                   # 가장 쉬운 문제의 번호 출력 위함
max_heap = []                   # 가장 어려운 문제의 번호 출력 위함
solved = {}                     # 문제가 풀렸는지 체크

for _ in range(int(stdin.readline())):      # N번 반복
    P, L = map(int, stdin.readline().split())
    heappush(min_heap, (L, P))
    heappush(max_heap, (-L, P))
    solved[P] = False
    
for _ in range(int(stdin.readline())):      # M번 반복
    cmd = list(stdin.readline().split())
    cmd[1] = int(cmd[1])
    
    if cmd[0] == 'recommend':
        if cmd[1] == 1:
            while solved[max_heap[0][1]]:   # max_heap에서 solved된 문제 모두 pop
                heappop(max_heap)
            print(max_heap[0][1])           # solved가 False인 가장 어려운 문제 출력
            
        elif cmd[1] == -1:
            while solved[min_heap[0][1]]:
                heappop(min_heap)
            print(min_heap[0][1])
    
    elif cmd[0] == 'add':
        cmd[2] = int(cmd[2])
        
        while solved[max_heap[0][1]]:       # 같은 번호 다른 난이도 문제 방지
            heappop(max_heap)
        while solved[min_heap[0][1]]:
            heappop(min_heap)
            
        heappush(min_heap, (cmd[2], cmd[1]))
        heappush(max_heap, (-cmd[2], cmd[1]))
        solved[cmd[1]] = False
    
    elif cmd[0] == 'solved':
        solved[cmd[1]] = True