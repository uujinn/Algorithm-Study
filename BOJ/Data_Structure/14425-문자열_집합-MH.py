from sys import stdin

answer = 0
sets = set()
N, M = map(int, stdin.readline().split())

for _ in range(N):
    sets.add(stdin.readline().rstrip())

for _ in range(M):
    if stdin.readline().rstrip() in sets:
        answer += 1

print(answer)