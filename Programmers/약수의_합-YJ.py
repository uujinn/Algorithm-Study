import math


def solution(n):
    answer = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            answer.append(i)
            if math.sqrt(n) != i:  # 제곱수 제외
                answer.append(n // i)
    return sum(answer)
