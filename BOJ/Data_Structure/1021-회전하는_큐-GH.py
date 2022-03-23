# N: 큐의 크기
# M: 뽑아내려고 하는 수의 개수
N, M = map(int, input().split())

# M_loca: 가장 처음 큐에서의 위치
M_loca = list(map(lambda x: int(x)-1, input().split()))

cnt = 0
for _ in range(M):
    if M_loca[0] < N-M_loca[0]:   # 왼쪽 회전
        cnt = cnt + M_loca[0]
        M_loca = list(map(lambda x: (x-M_loca[0]) % N-1, M_loca))
        del M_loca[0]
        N = N-1

    else:    # 오른쪽 회전
        cnt = cnt + (N - M_loca[0])
        M_loca = list(map(lambda x: (x+N-M_loca[0]) % N-1, M_loca))
        del M_loca[0]
        N = N-1

print(cnt)