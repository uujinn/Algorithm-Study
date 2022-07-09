n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]


dx = [1, 0]
dy = [0, 1]

dp[0][0] = 1
for i in range(n):
    for j in range(n):
        moved = arr[i][j]
        if moved > 0:
            if 0 <= i + moved < n:
                dp[i+moved][j] += dp[i][j]

            if 0 <= j + moved < n:
                dp[i][j+moved] += dp[i][j]

print(dp[-1][-1])
