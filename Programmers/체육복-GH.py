def solution(n, lost, reserve):
    
    # 여벌 체육복 있는 학생도 도난당할 수도 있음
    # 즉, lost와 reserve에 중복되는 값이 있다면 reserve에서 제외해야 함
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    # ㅇㅇ 왼쪽부터 탐색해 줄게
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)   
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    
    answer = n - len(set_lost)
    
    return answer