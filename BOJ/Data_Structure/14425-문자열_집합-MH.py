from sys import stdin

answer = 0
N, M = map(int, stdin.readline().split())

sets = list(stdin.readline().rstrip() for _ in range(N))
test = list(stdin.readline().rstrip() for _ in range(M))

for str in test:
    if str in sets:
        answer += 1

print(answer)