def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        default = 0
        for i in range(1, num+1):
            if not num % i: default += 1
        answer += num if not default % 2 else (-num)
    return answer

print(solution(13, 17))