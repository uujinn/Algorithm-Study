import sys

n = int(sys.stdin.readline())

d = [[0 for _ in range(10)] for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        d[i] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    else:
        for j in range(10):
            if j == 0:
                d[i][j] = d[i-1][1]

            elif j == 9:
                d[i][j] = d[i-1][8]

            else:
                d[i][j] = d[i-1][j-1] + d[i-1][j+1]

stairs = sum(d[n]) % 1000000000

print(stairs)
