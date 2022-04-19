def prime(num):
    for i in range(2, round(num**0.5)+1):
        if num % i == 0: return False
    return True
        
def solution(n):
    answer = 0
    for i in range(2, n+1):
        if prime(i): answer += 1
    return answer