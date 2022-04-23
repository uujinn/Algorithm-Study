from sys import stdin

n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))

for i in range(1, min(numbers) + 1):
    flag = True
    
    for num in numbers:
        if num % i != 0:
            flag = False
    if flag:
        print(i)
