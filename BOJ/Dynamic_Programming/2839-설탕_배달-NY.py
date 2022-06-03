import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n in [0,1,2,4,7]: return -1
    if n==3 or n==5: return 1
    else: 
        a = f(n-3)
        b = f(n-5)
        if a < 0: a = b
        if b < 0: b = a
        return min(a+1, b+1)
    
N = int(input())
print(f(N))