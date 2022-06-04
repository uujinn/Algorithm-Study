N = int(input())
dp = [0] * (N+1)
for i in range(3, N+1):
    if i in [4, 7]: continue
    elif i==3: dp[i] = 1
    elif i >= 5: 
        a = dp[i-3]
        b = dp[i-5]
        if a == 0: a=b
        if b == 0: b=a
        dp[i] = min(a+1, b+1)
print(-1 if dp[N]==0 else dp[N])