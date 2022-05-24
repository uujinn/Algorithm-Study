import sys
import math

input = sys.stdin.readline

def prime(n):
    answer = True

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            answer = False
            break

    return answer


N = int(input())
A = list(map(int, input().strip().split()))
answer = 1
dict = {}

for i in range(N):
    if prime(A[i]) and A[i] not in dict:
        dict[A[i]] = 1
        answer *= A[i]

answer = -1 if answer == 1 else int(answer)

print(answer)