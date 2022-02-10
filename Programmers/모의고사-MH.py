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

# 7점 받았어용 희희 correct에 각 학생들이 맞은 개수 넣어놓고 max 값 가진 학생의 인덱스를 answer에 넣어서 반환하는 방식입니다
# 저는 각 학생의 찍는 패턴을 문제에서 제시한 최대 길이로 맞춰놓고 시작했는데 % 연산자 통해서 계산하는 방식도 있더라구용