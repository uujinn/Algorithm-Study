from sys import stdin, setrecursionlimit
from itertools import combinations
setrecursionlimit(10 ** 6)

def GCD(x, y):
    if y == 0:
        return x
    return GCD(y, x % y)


for _ in range(int(stdin.readline())):
    nums = list(map(int, stdin.readline().split()))
    hap = 0
    
    for a, b in combinations(nums[1:], 2):
        if a < b:
            a, b = b, a
        hap += GCD(a, b)
    
    print(hap)