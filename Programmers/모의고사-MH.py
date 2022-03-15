def solution(answers):
    answer = []
    correct = [0, 0, 0]   
    supoja = [[1, 2, 3, 4, 5] * 2000,
              [2, 1, 2, 3, 2, 4, 2, 5] * 1250,
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000]
    
    for i, a in enumerate(answers):
        for j in range(3):
            if a == supoja[j][i]:
                correct[j] += 1
    
    for i, c in enumerate(correct):
        if c == max(correct):
            answer.append(i + 1)
    
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))