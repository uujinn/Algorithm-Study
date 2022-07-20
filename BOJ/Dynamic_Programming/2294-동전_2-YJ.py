N, K = map(int, input().split())
coins = sorted([int(input()) for _ in range(N)])

dp = [10001] * (K+1)
dp[0] = 0

for i in range(N):
    for j in range(coins[i], K+1):
        dp[j] = min(dp[j], dp[j-coins[i]] + 1)

dp[-1] = dp[-1] if dp[-1] != 10001 else -1
print(dp[-1])
