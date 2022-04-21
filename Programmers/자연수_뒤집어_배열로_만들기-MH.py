def solution(n):
    answer = [i for i in str(n)[::-1]]
    return answer

print(solution(12345))