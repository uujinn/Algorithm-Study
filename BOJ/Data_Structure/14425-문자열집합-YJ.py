from sys import stdin

N, M = map(int,stdin.readline().rstrip().split())
S = [0] * N
inputs = [0] * M

answer = 0

for i in range(N):
    S[i] = stdin.readline().rstrip()

for i in range(M):
    inputs[i] = stdin.readline().rstrip()

for s in inputs:
    if s in S:
        answer += 1


print(answer)
