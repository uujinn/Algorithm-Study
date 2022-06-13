from sys import stdin
import math


def four_squares(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return 1

    for i in range(1, int(math.sqrt(n) + 1)):
        if int(math.sqrt(n - i ** 2)) == math.sqrt(n - i ** 2):
            return 2

    for i in range(1, int(math.sqrt(n) + 1)):
        for j in range(1, int(math.sqrt(n - i ** 2)) + 1):
            if int(math.sqrt(n - i ** 2 - j ** 2)) == math.sqrt(n - i ** 2 - j ** 2):
                return 3

    return 4


# main
n = int(stdin.readline())
print(four_squares(n))
