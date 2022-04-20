def solution(n):
    answer = ''
    if n % 2 == 0:
        answer = '수박' * int(n / 2)
    else:
        answer = '수' + '박수' * int(n / 2)
    return answer


print(solution(1))
