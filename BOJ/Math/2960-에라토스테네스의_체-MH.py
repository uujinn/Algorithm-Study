from sys import stdin

N, K = map(int, stdin.readline().split())
arr = [False, False] + [True] * (N - 1)
count = 0

for i in range(2, N + 1):
    if arr[i]:        
        arr[i] = False
        count += 1
        
        if count == K:
            print(i)
            break
        
        for j in range(i * 2, N + 1, i):
            if arr[j]:
                arr[j] = False
                count += 1
            
            if count == K:
                print(j)
                break