n = int(input())
dp = [0,1]
for i in range(2, n+1):
    min_val = int(50000 ** 0.5)
    j=1
    while j**2 <= i:
        min_val = min(min_val, dp[i-(j**2)])
        j += 1
    dp.append(min_val+1)
print(dp[n])