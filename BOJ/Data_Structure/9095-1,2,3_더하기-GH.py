import sys
input = sys.stdin.readline

list = [0] * 11
list[1] = 1
list[2] = 2
list[3] = 4

for i in range(4, 11):
    list[i] = sum(list[i-3:i])

T = int(input())

for _ in range(T):
    print(list[int(input())])