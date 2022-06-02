from sys import stdin
def f(n):
    if n<=1: return n
    else:
        return f(n-1) + f(n-2)

n = int(stdin.readline())
print(f(n))