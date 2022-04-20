def solution1(n):
    answer = 0
    while n > 0:
        answer += (n % 10)
        n //= 10  
    return answer

def solution2(n):
    if n < 10:
        return n
    return (n % 10) + solution2(n // 10)

print(solution2(123))