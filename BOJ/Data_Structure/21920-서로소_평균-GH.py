import sys
import math

input = sys.stdin.readline

answer = []
N = int(input())
meow = list(map(int, input().split()))
X = int(input())

for num in meow:
    if math.gcd(num, X) == 1:
        answer.append(num)

print(int(sum(answer)/len(answer)))