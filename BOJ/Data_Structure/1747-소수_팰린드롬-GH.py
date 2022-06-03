import sys
import math

input = sys.stdin.readline

def primeNumber(num):
    if num == 2 or num == 3:
        return True
    elif num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def Palindrome(num):
    array = str(num)
    if array == array[::-1]:
        return True
    else:
        return False

N = int(input())

for i in range(N, 20000000):
    if primeNumber(i) and Palindrome(i):
        print(i)
        break