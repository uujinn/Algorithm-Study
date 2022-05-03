from sys import stdin

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)
    
    
for _ in range(int(stdin.readline())):
    A, B = map(int, stdin.readline().split())
    if A < B: A, B = B, A    
    gcd = GCD(A, B)
    print(A * B // gcd)