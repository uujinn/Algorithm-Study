def solution(n):
    answer = n ** (1/2)
    return int((answer + 1) ** 2) if answer == int(answer) else -1

print(solution(3))