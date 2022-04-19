def solution(n):
    answer = ''

    for idx in range(n):
        if idx % 2 == 0:
            answer += '수'
        else:
            answer += '박'

    return answer