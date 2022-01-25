def solution(numbers):
    answer = 0
    for num in numbers:
        answer += num
    return (45 - answer)

print(solution([1,2,3,4,6,7,8,0]))