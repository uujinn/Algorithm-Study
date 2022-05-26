from sys import stdin

def prime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
def palindrome(n):
    return True if int(str(n)[::-1]) == n else False
    
N = int(stdin.readline())
i = 0
while True:
    if prime(N+i) and palindrome(N+i):
        print(N+i)
        break
    i += 1