from sys import stdin

for _ in range(int(stdin.readline())):
    answer = 0

    N, M = map(int, stdin.readline().split())
    importance = list(map(int, stdin.readline().split()))
    index = list(range(len(importance)))

    while True:
        if importance[0] == max(importance):
            answer += 1
            if index[0] == M: # 파악해야하는 인쇄물
                print(answer)
                break
            else:
                importance.pop(0) 
                index.pop(0)
        
        else: # 재배치
            importance.append(importance.pop(0))
            index.append(index.pop(0))