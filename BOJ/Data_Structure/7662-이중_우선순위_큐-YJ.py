from sys import stdin
from heapq import heappush, heappop
from tabnanny import check

counts = {} # Counter 역할

for i in range(int(stdin.readline())): # T
    min_h = [] # 최소 힙
    max_h = [] # 최대 힙

    for i in range(int(stdin.readline())): # K
        command, n = map(str, stdin.readline().rstrip().split())
        if command == "I":
            # if counts.get(int(n)): 
            #     counts[int(n)] += 1
            # else:
            #     counts[int(n)] = 1

            heappush(min_h, int(n))
            heappush(max_h, -int(n)) # 최대 힙은 음수로 넣어줌
            # print(counts)
            # print(min_h)
            # print(max_h)
        
        elif command == "D":
            if n == "1": # Q에서 최댓값을 삭제하는 연산
                if max_h:
                    tmp = -heappop(max_h) # 최대힙 사용했으므로 음수 붙여줌
                    min_h.remove(tmp)
                # if counts[tmp] > 0: # Q가 비어있으면 무시
                #     counts[tmp] -= 1 
                #     print(counts)
            elif n == "-1": #Q에서 최솟값을 삭제하는 연산
                # print(min_h)
                if min_h:
                    tmp = heappop(min_h)
                    max_h.remove(-tmp)
                # print(tmp)
                # print(f'counts: {counts}')
                # if counts[tmp] > 0: # Q가 비어있으면 무시
                #     counts[tmp] -= 1
                #     print(counts)

    print(counts)
    if not min_h: # 힙이 비어있으면
        print("EMPTY")
    else:
        print(-heappop(max_h), heappop(min_h))
