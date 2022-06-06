n = int(input())
fib = [0] * (n+1)
for i in range(1, n+1):
    if i==1: fib[i] = 1
    elif i > 1:
        fib[i] = fib[i-1] + fib[i-2]
print(fib[n])