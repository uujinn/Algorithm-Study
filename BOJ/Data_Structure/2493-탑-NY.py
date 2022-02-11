from sys import stdin
N = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))

def recursion(num, i):
    if num <= towers[i-1]: 
        print(i, '', end='')
        return
    elif i == 1:
        print(0, "", end='')
    else: 
        recursion(num, i-1)

print(0, "", end="")
for i in range(1, len(towers)):
    recursion(towers[i], i)
