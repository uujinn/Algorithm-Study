from sys import stdin 

n = int(stdin.readline())
fib = []

for i in range(n + 1):
    if i in [0, 1]:
        temp = i
    elif i == 2:
        temp = 1
    else:
        temp = fib[-1] + fib[-2]
    fib.append(temp)

print(fib[-1])