def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    for l in lost[:]:
        if l in reserve: 
            lost.remove(l)
            reserve.remove(l)
            
    answer = n - len(lost)
    index = 0
    for r in reserve:
        for i in range(index, len(lost)):
            if lost[i]==r or lost[i]+1==r or lost[i]-1==r:
                answer += 1
                index = i + 1
                break
    return answer

print(solution(5, [2, 4], [1, 3, 5]))