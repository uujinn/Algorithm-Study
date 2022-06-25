from sys import stdin

n = int(stdin.readline())
tiles = [0] * 1001
tiles[1], tiles[2] = 1, 3;

for i in range(3, n + 1):
    tiles[i] = tiles[i - 1] + tiles[i - 2] * 2

print(tiles[n] % 10007)