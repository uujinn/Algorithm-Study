from sys import stdin

stack = []
num = int(stdin.readline())
tops = list(map(int, stdin.readline().split()))
recieve = []

for i, t in enumerate(tops):    
    for j in reversed(range(i)):
        if tops[j] >= t:
            recieve.append(j + 1)
            break
    
    if len(recieve) - 1 < i:
        recieve.append(0)

print(recieve)