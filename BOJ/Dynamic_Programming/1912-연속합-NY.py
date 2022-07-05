from sys import stdin
n = int(stdin.readline())
a = [0]
a += list(map(int, stdin.readline().split()))
dp = [0] * (n+1)
maximum = a[1]

for i in range(1, n+1):
    dp[i] = a[i]
    if dp[i] < dp[i-1] + a[i]: 
        dp[i] = dp[i-1] + a[i]
    maximum = max(maximum, dp[i])

print(maximum)
