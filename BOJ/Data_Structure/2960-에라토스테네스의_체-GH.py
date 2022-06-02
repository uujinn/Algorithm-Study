import sys, math

input = sys.stdin.readline

N, K = map(int, input().split())
num = [1] * (N+1)
answer = 0

for i in range(2, N+1):
  for j in range(i, N+1, i):
    if num[j]:
      num[j] = 0
      answer += 1

      if answer == K:
        print(j)
        break