def solution(n):
    answer = 0
    for i in range(1,  int(n**(1/2)) + 1): 
        if not n % i: 
            answer += i
            if i != n//i: answer += n//i
    return answer