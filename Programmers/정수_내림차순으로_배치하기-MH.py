def solution(n):
    numbers = sorted(str(n), reverse=True)
    return int(''.join(numbers))

print(solution(118372))