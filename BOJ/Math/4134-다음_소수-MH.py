from sys import stdin

cases = []
for _ in range(int(stdin.readline())):
    cases.append(int(stdin.readline()))

num = max(cases) * 2
arr = [False, False] + [True] * (num - 1)

for i in range(2, int(num ** 0.5) + 1):
    if arr[i]:        
        for j in range(i * 2, num + 1, i):
            if arr[j]:
                arr[j] = False

for n in cases:
    for i in range(n, num + 1):
        if arr[i]:
            print(i)
            break