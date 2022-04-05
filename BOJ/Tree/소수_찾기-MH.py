def solution(n):
    arr = []
        
    for i in range(2, n + 1):
        if i in arr:
            continue
        
        for j in range(2 * i, n + 1, i):
            if i in arr:    continue
            else:           arr.append(j)    
        
    return (n - 1) - len(set(arr))

print(solution(5))