def solution(numbers):
    
    all_numbers = {i for i in range(10)}
    answer = sum(all_numbers - set(numbers)) # 차집합
    
    return answer
