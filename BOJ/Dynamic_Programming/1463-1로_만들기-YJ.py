from cmath import e
from sys import stdin

N = int(stdin.readline())

dp = [0] * (N+1)  # N을 1로 만드는 최소 연산 횟수

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1  # 연산 횟수 추가임 (1 빼줄 때로 가정)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)  # 연산 횟수 추가임
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # 연산 횟수 추가임


print(dp[N])
