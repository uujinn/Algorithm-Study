from sys import stdin

def DFS(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return DFS(n - 1) + DFS(n - 2) + DFS(n - 3)


for _ in range(int(stdin.readline())):
    print(DFS(int(stdin.readline())))