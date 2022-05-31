def solution(n):
    numbers = {0: "1", 1: "2", 2: "4"}
    answer = ""
    while n:
        n, tmp = divmod(n-1, 3)
        answer += numbers[tmp]
    return answer[::-1]
