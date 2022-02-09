def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
    
        sliced = sorted(array[i-1:j]) # 슬라이싱 & 정렬
        answer.append(sliced[k-1])
    
    return answer
