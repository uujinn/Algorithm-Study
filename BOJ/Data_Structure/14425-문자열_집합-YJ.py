from sys import stdin

input = stdin.readline().rstrip()

N, M = map(int,input.split())
S = [0] * N
inputs = [0] * M

answer = 0

for i in range(N):
    S[i] = input

for i in range(M):
    inputs[i] = stdin.readline().rstrip()

for s in inputs:
    if s in S:
        answer += 1

print(answer)