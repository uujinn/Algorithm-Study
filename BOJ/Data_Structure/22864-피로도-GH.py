a, b, c, m = map(int, input().split())

pirodo = 0
work = 0

for i in range(24):
    if pirodo < 0 :
        pirodo = 0

    if pirodo + a > m:
        pirodo -= c
        continue

    else:
        pirodo += a
        work += b

print(work)