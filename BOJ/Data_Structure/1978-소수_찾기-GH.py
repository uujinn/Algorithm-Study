import math
import sys

input = sys.stdin.readline
n = int(input(''))

count_chk = 0
count = 0

num = list(map(int, input('').split()))

while (1):
    check = 0
    if num[count_chk] > 1:
        for i in range(2, int(math.sqrt(num[count_chk])) + 1):
            if num[count_chk] % i == 0:
                check = 1
        if check == 0:
            count = count + 1

    count_chk = count_chk + 1

    if count_chk == n:
        break

print(count)