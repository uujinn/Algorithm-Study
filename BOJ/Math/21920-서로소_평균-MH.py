from sys import stdin, setrecursionlimit
import math
setrecursionlimit(10 ** 6)

def GCD(x, y):
    if y == 0:
        return x
    return GCD(y, x % y)


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
X = int(stdin.readline())

seoroso = []
for num in nums:
    x, y = max(num, X), min(num, X)
    
    if GCD(x, y) == 1:
    # if math.gcd(num, X) == 1:
        seoroso.append(num)
        
print(sum(seoroso) / len(seoroso))