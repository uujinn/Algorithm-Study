def solution(num):
    for cnt in range(500):
        if num == 1:
            return cnt
        
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    
    return -1

print(solution(6))
print(solution(626331))