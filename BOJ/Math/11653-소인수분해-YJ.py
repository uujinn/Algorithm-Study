import math
N = int(input())

for i in range(2, int(math.sqrt(N)) + 1):
    while N % i == 0:
        print(i)
        N //= i

# print(N)
if N >= 2:  # N이 이제 소수 / 원래 소수
    print(N)
