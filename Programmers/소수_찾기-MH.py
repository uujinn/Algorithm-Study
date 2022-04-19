def solution(n):
    arr = list(range(n + 1))
    arr[1] = 0                        # 1은 소수 판별하지 않음
    # arr : [0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for i in range(n + 1):
        if arr[i] == 0:
            continue
        
        for j in range(i * 2, n + 1, i):
            arr[j] = 0
    
    # arr[2:] : [2, 3, 0, 5, 0, 7, 0, 0, 0]
    return len(arr[2:]) - arr[2:].count(0)

print(solution(10))