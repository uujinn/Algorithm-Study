def solution(n):
    numbers = {0: "1", 1: "2", 2: "4"}
    answer = ""
    while n:
        n, m = divmod(n-1, 3)
        answer += numbers[m]
    return str("".join(list(reversed(answer))))
