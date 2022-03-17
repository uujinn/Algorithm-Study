def solution(arr):
    answer = []
    for i in arr:
        if not answer or i != answer[-1]:
            answer.append(i)
    return answer

print(solution([1,1,3,3,0,1,1]))