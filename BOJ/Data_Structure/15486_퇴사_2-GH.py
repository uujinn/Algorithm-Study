import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]
max_ = 0

for i in range(N):
    max_ = max(max_, dp[i])
    if i + arr[i][0] > N:
        continue
    dp[i + arr[i][0]] = max(max_ + arr[i][1], dp[i + arr[i][0]])

print(max(dp))