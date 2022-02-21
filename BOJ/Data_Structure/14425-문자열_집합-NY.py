from sys import stdin
N, M = map(int, stdin.readline().split())
s = set()
cnt = 0
for _ in range(N):
    s.add(stdin.readline().rstrip())
    
for _ in range(M):
    if stdin.readline().rstrip() in s:
        cnt += 1
print(cnt)