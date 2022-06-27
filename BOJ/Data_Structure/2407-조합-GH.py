import math, sys

input = sys.stdin.readline

n, m = map(int, input().split())
x = math.factorial(n)
y = (math.factorial(n - m)) * (math.factorial(m))
print(x // y)