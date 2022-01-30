def solution(a, b):
    answer = 0
    for A,B in zip(a,b):
        answer += A * B
    return answer
