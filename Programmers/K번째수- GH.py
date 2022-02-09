def solution(array, commands):
    answer = []
    
    for x in commands:
        i, j, k = x
        
        new = array[i-1:j]
        new.sort()
        answer.append(new[k-1])
    
    return answer