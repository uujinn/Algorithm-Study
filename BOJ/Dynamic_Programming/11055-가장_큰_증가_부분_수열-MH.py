from sys import stdin

N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

hap = [0] * N
for i in range(N):
    for j in range(i):        
        if nums[j] < nums[i]:
            hap[i] = max(hap[i], hap[j])
                        
    hap[i] += nums[i]
    
print(max(hap)) 