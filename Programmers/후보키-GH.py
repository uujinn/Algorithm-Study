from itertools import combinations


def solution(relation):
    
    length = len(relation)
    col_length = len(relation[0])
    com = []
    for i in range(1, col_length+1):
        com.extend(combinations(range(col_length), i))
        
    unique = []
    for i in com:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        if len(set(tmp)) == length: # 유일성 체크
            unique.append(i)

    answer = set(unique)

    for i in range(len(unique)):
        for j in range(i+1, len(unique)):

            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)