def solution(progresses, speeds):
    remains, answer = [], []
    
    for p, s in zip(progresses, speeds):
        temp = (100 - p) / s
        temp = int(temp) if temp % 1 == 0 else int(temp) + 1
        remains.append(temp)
    
    days = remains[0]
    features = 1
    for i in range(1, len(remains) + 1):
        if i == len(remains):
            answer.append(features)
            break
        
        if days >= remains[i]:
            features += 1
        else:
            answer.append(features)
            features = 1
            
        if remains[i] > days:
            days = remains[i]
            
    return answer

print(solution([93, 30, 55], [1, 30, 5]))