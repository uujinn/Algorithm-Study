def solution(_numbers):

    numbers = [str(n) for n in _numbers]
    print(numbers)
    
    max_length = len(str(max(_numbers)))
    print(max_length)
    
    answer = [[-1] * max_length for _ in range(len(numbers))]
    print(answer)
    
    for i, n in enumerate(numbers):
        for j in range(len(n)):
            answer[i][j] = int(n[j])
    # answer : [['3', -1], ['3', '0'], ['3', '4'], ['5', -1], ['9', -1]]
    
    answer = sorted(answer, key=lambda x: (-x[0], -x[1]))
    
    
    return answer

# print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))