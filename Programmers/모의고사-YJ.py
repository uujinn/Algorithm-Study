def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first_result, second_result, third_result = 0, 0, 0

    for i, num in enumerate(answers):
        if num == first[i % len(first)]: first_result += 1
        if num == second[i % len(second)]: second_result += 1
        if num == third[i % len(third)]: third_result += 1

    if max(first_result, second_result, third_result) == first_result:
        answer.append(1)
    if max(first_result, second_result, third_result) == second_result:
        answer.append(2)
    if max(first_result, second_result, third_result) == third_result:
        answer.append(3)
    
    return answer

print(solution([1,2,3,4,5]))