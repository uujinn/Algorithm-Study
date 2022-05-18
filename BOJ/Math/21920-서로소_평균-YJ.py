import math

answer = []
N = int(input())
arr = list(map(int, input().split()))
X = int(input())

for num in arr:
    if math.gcd(num, X) == 1:
        answer.append(num)

print(int(sum(answer)/len(answer)))
