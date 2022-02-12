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

# 15점이나 받았어요 대박
# 사실 테스트 케이스 자꾸 틀려서 질문하기 창에서 팁 좀 얻었어요 엉엉..
# 더 나은 코드를 짜는 그 날까지.. 화이팅..