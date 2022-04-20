from sys import stdin

def find_all(n):
    nums = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            nums.update([i, n//i])
    return nums
    
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
sets = list(set() for _ in range(n))
for idx, num in enumerate(nums):
    sets[idx].update(find_all(num))
temp = sets[0]
for i in range(1, n):
    temp = temp & sets[i]
result = list(temp)
for r in sorted(result):
    print(r)