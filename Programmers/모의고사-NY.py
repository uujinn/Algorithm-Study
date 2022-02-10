def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    temp = [0, 0, 0]
    result = []
    
    for i, answer in enumerate(answers):
        if answer == first[i%5]: temp[0] += 1
        if answer == second[i%8]: temp[1] += 1
        if answer == third[i%10]: temp[2] += 1
        
    for i in range(3):
        if temp[i] == max(temp): result.append(i+1)
    
    return result

print(solution([1,2,3,4,5]))