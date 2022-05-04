import math

M = int(input())
N = int(input())

def is_sosu(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

arr = []
for num in range(M, N+1):
    if num == 1:
        continue
    elif is_sosu(num):
        arr.append(num)

if not arr:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))


    