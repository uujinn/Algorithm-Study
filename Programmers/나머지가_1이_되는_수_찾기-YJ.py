import math

def solution(n):
    n = n -1 
    if n % 2 == 0: # 짝수라면
        return 2
    else: # 홀수라면
        for i in range(2, int(math.sqrt(n) + 1)): 
            if n % i == 0: # 소수가 아니라면
                return i
    
        return n # 소수라면

print(solution(10))