from sys import stdin

tileing = [0, 1, 2]
for i in range(3, 1001):
    tileing.append(tileing[i - 1] + tileing[i - 2])

n = int(stdin.readline())
print(tileing[n] % 10007)