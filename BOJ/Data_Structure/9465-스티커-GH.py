import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
  N = int(input())
  arr = [list(map(int, input().rstrip().split())) for _ in range(2)]

  dp = [[0] * N for _ in range(2)]
  dp[0][0] = arr[0][0]
  dp[1][0] = arr[1][0]

  for j in range(1, N):

    for i in range(2):
      if i == 0:
        dp[i][j] = max(dp[i][j-1], dp[i+1][j-1] + arr[i][j])
      elif i == 1:
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + arr[i][j])

  print(max(dp[0][N-1], dp[1][N-1]))