import enum
from sys import stdin

for _ in range(int(stdin.readline())):
    answer = 0

    N, M = map(int, stdin.readline().split())
    enumeration = list(enumerate(map(int, stdin.readline().split()))) # importance와 index 한번에 저장
    
    while True:
        if enumeration[0][1] == max(enumeration, key=lambda x: x[1])[1]:
            answer += 1
            if enumeration[0][0] == M: # 파악해야하는 인쇄물
                print(answer)
                break
            else:
                enumeration.pop(0)
        
        else: # 재배치
            enumeration.append(enumeration.pop(0))