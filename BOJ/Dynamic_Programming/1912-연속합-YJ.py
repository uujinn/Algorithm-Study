n = int(input())

dp = [0] * n

arr = list(map(int, input().split()))

for idx, i in enumerate(arr):
    dp[idx] = max(dp[idx-1] + i, i)

print(max(dp))
