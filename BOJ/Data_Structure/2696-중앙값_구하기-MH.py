from sys import stdin

for _ in range(int(stdin.readline())):          # 테스트 케이스 개수 T
    nums = []
    M = int(stdin.readline())                   # 수열의 크기
    
    for i in range(M // 10 + 1):
        nums += list(map(int, stdin.readline().split()))    
    print(M // 2 + 1)                           # 중앙값의 개수
    
    for i in range(M):
        if i == 0:
            print(nums[0], end=' ')
        elif i % 2 == 0:
            print(sorted(nums[:i + 1])[i // 2], end=' ')
        
        if i != 0 and (i + 1) % 20 == 0:
            print()