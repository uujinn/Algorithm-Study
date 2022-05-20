import math
from itertools import combinations

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    answer = 0
    c = combinations(arr[1:], 2)
    for a, b in c:
        answer += math.gcd(a, b)

    print(answer)
