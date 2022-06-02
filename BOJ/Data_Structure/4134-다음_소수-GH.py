import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    std = int(input().rstrip())
    while(True):
        for j in range(2, std):
            if std % j == 0:
                break
        else:
            print(std)
            break
        std += 1