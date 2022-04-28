import sys

input = sys.stdin.readline


def getGcd(a, b):
    if a == 0:
        return b
    return getGcd(b % a, a)

n = int(input())

num = list(map(int, sys.stdin.readline().split()))
g = getGcd(num[0], getGcd(num[1], num[-1]))

for i in range(1, g // 2 + 1):

    if g % i == 0:
        print(i)

print(g)