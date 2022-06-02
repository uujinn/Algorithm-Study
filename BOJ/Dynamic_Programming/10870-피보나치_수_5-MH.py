from sys import stdin

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(stdin.readline())
print(fibonacci(n))