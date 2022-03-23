def solution(n):
    answer = ''
    while n > 0:
        quotient, remainder = divmod(n, 3)
        answer += str(remainder)
        n = quotient

    return int(answer, base=3)