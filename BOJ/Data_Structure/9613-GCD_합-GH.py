import sys
from itertools import combinations

input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, (x % y)
    return x


n = int(input())
arr = []
result = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    arr = arr[::-1]
    del arr[len(arr) - 1]
    nCr = combinations(arr, 2)

    for i in nCr:
        result += gcd(i[0], i[1])
    print(result)
    result = 0