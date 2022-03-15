def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
    reserve_student = set(reserve) - set(lost) 
    lost_student = set(lost) - set(reserve)
    
    for i in reserve_student:
        if i-1 in lost_student: # 왼쪽에 있는 학생이 체육복이 없다면 빌려줌
            lost_student.remove(i-1)
        elif i + 1 in lost_student: # 오른쪽 학생
            lost_student.remove(i+1)
    
    return n - len(lost_student)