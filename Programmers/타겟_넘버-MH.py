from itertools import combinations

def solution(numbers, target):
    answer, comb = [], []
    index = [i for i in range(len(numbers))]
    
    for i in range(1, len(numbers)):
        comb += list(combinations(index, i))
    
    answer.append(sum(numbers))
    for c in comb:
        temp = 0
        
        for i in range(len(numbers)):
            if i in c:
                temp -= numbers[i]
            else:
                temp += numbers[i]
        answer.append(temp)
    
    return answer.count(target)

print(solution([1, 1, 1, 1, 1],	3))