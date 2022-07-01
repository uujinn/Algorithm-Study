from sys import stdin
A = int(stdin.readline())
A_arr = list(map(int, stdin.readline().split()))

dp = [0] * A
answer = 0

for i in range(0, A):
    count = 0
    for j in range(0, i):
        if A_arr[i] > A_arr[j] and count < dp[j]: count = dp[j]
    dp[i] = count + 1
    answer = max(dp[i], answer)
print(answer)