from sys import stdin

N = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
indexs = [] # 현재 신호를 보내고 있는 탑의 인덱스
answer = [0] * N # default 값 = 0

for i, tower in enumerate(reversed(towers)):
    index = len(towers) - i - 1   # 탑의 인덱스 4, 3, 2, 1, 0
    while indexs: # 현재 쏘고 있는 신호 있음
        # print(f'{index}: {tower}')
        # print(indexs)
        # print(towers[indexs[-1]])
        if tower > towers[indexs[-1]]: # 해당 신호를 보낸 탑의 높이보다 수신할 차례인 탑이 키가 크다면 
            answer[indexs.pop()] = index + 1 # 신호 자리에 해당 신호를 수신한 탑의 번호 저장 5, 4, 3, 2, 1
        else: # 수신 불가 
            break
    indexs.append(index) # 다음 탑 신호 인덱스 추가

print(" ".join(map(str, answer)))
