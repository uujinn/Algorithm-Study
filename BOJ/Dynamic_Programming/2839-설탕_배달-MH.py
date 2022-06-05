from sys import stdin

N = int(stdin.readline())
count = 0

while True:
    if N % 5 == 0:
        count = count + (N // 5)
        print(count)
        break
    
    N -= 3
    count += 1
    
    if N < 0:
        print(-1)
        break