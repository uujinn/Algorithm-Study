from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

hap = [0] * n
hap[0] = nums[0]

for i in range(n):
    hap[i] = max(nums[i], hap[i - 1] + nums[i])
    
print(max(hap))