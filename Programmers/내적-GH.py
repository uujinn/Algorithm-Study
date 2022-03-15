def solution(a, b):
    
    answer = 0
    
    # 리스트 각각의 index에 대응하는 수를 곱한 후, 모두 더함
    
    for i in range(len(a)):
        answer += a[i] * b[i]
        
    return answer