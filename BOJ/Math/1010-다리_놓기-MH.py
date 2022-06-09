from sys import stdin

for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    
    temp = 1
    a = min(N, M - N)
    for i in range(a):
        temp *= (M - i)
        temp /= (a - i)
        print(M - i)
        print(a - i)
    
    print(int(temp))