from sys import stdin

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False
    

num = int(stdin.readline())
    
while True:
    if num == 0 or num == 1:
        num += 1 
    elif is_prime(num) and is_palindrome(num):
        print(num)
        break
    else:
        num += 1