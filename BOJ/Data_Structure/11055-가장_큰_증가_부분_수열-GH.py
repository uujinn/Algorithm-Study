import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = arr[i]
    if arr[i] > arr[i-1]:
        dp[i] = arr[i-1] + arr[i]

    for j in range(i-1, -1, -1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], arr[i] + dp[j])

print(max(dp))