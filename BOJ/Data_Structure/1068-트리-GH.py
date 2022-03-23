def DFS(x):
    global count
    if len(map[x]) == 0:
        count = count + 1
    else:
        for i in map[x]:
            DFS(i)


count = 0
n = int(input())
x = list(map(int, input().split()))

map = [[] for _ in range(52)]

for _ in range(0, n):
    if (x[_] == -1):
        start = _
    else:
        map[x[_]].append(_)

y = int(input())

for i in range(n):
    if y in map[i]:
        map[i].remove(y)
if start != y:
    DFS(start)

print(count)