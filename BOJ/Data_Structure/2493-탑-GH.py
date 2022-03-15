import sys
input = sys.stdin.readline
 
N = int(input())
arr = list(map(int, input().split()))
result = [0] * N
 
for i in range(1, N):
    target = i - 1
    while target != -1:
        if arr[target] >= arr[i]:
            result[i] = target+1
            break
        else:
            target = result[target]-1
 
print(*result)