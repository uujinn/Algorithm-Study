def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp = []
        for a, b in zip(arr1[i], arr2[i]):
            temp.append(a + b)
        answer.append(temp)
        
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))