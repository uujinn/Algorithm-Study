def solution1(s):
    return int(s)

def solution2(s):
    answer = 0
    
    for i, c in enumerate(s[::-1]):
        if c == '+': continue
        elif c == '-': answer *= (-1)
        else:
            answer += (10**i * int(c))
        
    return answer

print(solution2('+1234'))