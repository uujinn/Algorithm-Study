from calendar import c
from sys import stdin

N = int(stdin.readline())
gamePan = [list(map(int, stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]        # i, j까지 올 수 있는 경우의 수를 저장
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break
        
        current = gamePan[i][j]
        if j + current < N:
            dp[i][j + current] += dp[i][j]
        if i + current < N:
            dp[i + current][j] += dp[i][j]