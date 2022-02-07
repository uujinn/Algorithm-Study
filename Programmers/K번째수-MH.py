def solution(array, commands):
    answer = []
    
    for com in commands:
        i, j, k = com[0] - 1, com[1] - 1, com[2] - 1
        
        temp = array[i:j + 1]
        temp.sort()
        index = k % len(temp)        
        answer.append(temp[index])
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))