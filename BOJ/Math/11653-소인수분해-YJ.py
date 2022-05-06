import math
N = int(input())
original = N

for i in range(2, int(math.sqrt(N)) + 1):
    while N % i == 0:
        print(i)
        N //= i

# print(N)
if N >= 2:  # 소수
    print(N)
