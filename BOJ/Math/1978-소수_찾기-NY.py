from sys import stdin
N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
count = 0
for n in nums:
    if n == 2 or n == 3: count += 1
    for i in range(2, int(n**0.5)+1):
        if not n % i: break
        else: 
            if i == int(n**0.5): count += 1
print(count)