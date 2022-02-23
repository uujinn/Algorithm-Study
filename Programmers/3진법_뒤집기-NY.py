def solution(n):
    answer = 0
    three_num = ""
    while n != 0:
        three_num += str(n % 3)
        n //= 3
    length = len(three_num)
    for i in range(length): answer += int(three_num[i]) * 3 ** (length-1-i)
    return answer
    
print(solution(45))