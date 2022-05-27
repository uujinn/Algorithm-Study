import math

N = int(input())


def is_sosu(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


while True:
    if list(str(N)) == list(reversed(str(N))):
        if is_sosu(N):
            print(N)
            break
    else:
        pass
    N += 1
