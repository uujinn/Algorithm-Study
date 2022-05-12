from sys import stdin

N, K = map(int, stdin.readline().split())
arr = [False, False] + [True] * (N - 1)
count = 0

for i in range(2, int(N ** 0.5) + 1):
    if arr[i]:
        count += 1
        if count == K:
            print(i)
            break
        
        for j in range(i * 2, N + 1, i):
            print('count : ', end='')
            print(count, end=', ')
            print(j)
                
            if arr[j]:
                count += 1
                
            arr[j] = False
            
            if count == K:
                print(j)
                break
            
            # print('count : ', end='')
            # print(count)