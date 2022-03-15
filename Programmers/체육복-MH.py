def solution(n, _lost, _reserve):
    lost = sorted([x for x in _lost if x not in _reserve])      # 정렬하고 여벌옷을 가져오고 도난당한 학생 체크
    reserve = sorted([x for x in _reserve if x not in _lost])
    answer = n - len(lost)
    
    for l in lost:       
        for x in [-1, 1]:
            if l + x in reserve:
                reserve.remove(l + x)
                answer += 1
                break
            
    return answer

print(solution(3, [1, 2], [2, 3]))