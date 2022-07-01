from sys import stdin

N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

length = [1] * N
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            length[i] = max(length[i], length[j] + 1 )
        
print(max(length))