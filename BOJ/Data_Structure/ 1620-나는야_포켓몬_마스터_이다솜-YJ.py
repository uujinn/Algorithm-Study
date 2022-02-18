from sys import stdin

N, M = map(int, stdin.readline().split())

dogam = {}
indexs = [0] * N

for i in range(N):
    name = stdin.readline().rstrip()
    dogam[name] = i
    indexs[i] = name

for _ in range(M):
    q = stdin.readline().rstrip()
    if q.isdigit():
        print(indexs[int(q)-1])
    else:
        print(dogam[q] + 1)