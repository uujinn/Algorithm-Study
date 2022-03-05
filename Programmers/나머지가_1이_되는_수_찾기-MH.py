def solution(n):    
    return [i for i in range(2, n) if n % i == 1][0]