import sys, math

input = sys.stdin.readline

n = int(input())
list = [0] * (n + 1)
list[0], list[1] = 0, 1

for i in range(2, n+1):
    min_value = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        min_value = min(min_value, list[i - j ** 2])
    list[i] = min_value + 1
print(list[n])