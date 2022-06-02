import math

T = int(input())


def is_sosu(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


for i in range(T):
    n = int(input())
    while True:
        if n == 0 or n == 1:
            n += 1
        elif is_sosu(n):
            print(n)
            break
        else:
            n += 1
