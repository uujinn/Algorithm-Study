def solution(numbers, hand):
    answer = ''
    left_numbers = [1, 4, 7] #무조건 왼쪽인 숫자들 -> 이 배열 안에 있는 숫자라면 바로 L 추가
    right_numbers = [3, 6, 9] #무조건 오른쪽인 숫자들 -> 이 배열 안에 있는 숫자라면 바로 R 추가
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 12] # *와 #는 10과 12로 대체
    L = 10
    R = 12
    
    for number in numbers:
        if number in left_numbers: 
            L = number
            answer += "L"
        elif number in right_numbers:
            R = number
            answer += "R"
        else: 
            L_index = keys.index(L) #O(1)복잡도라서 리스트 인덱스 함수로 해당 숫자의 위치 뽑아냄
            R_index = keys.index(R)
            number_index = keys.index(number) 
            distance_L = abs(number_index//3 - L_index//3) + abs(number_index%3 - L_index%3) # //3 거리 차이 절대값은 높이. %3 거리 차이 절대값은 양옆으로 이동 시 발생하는 거리.
            distance_R = abs(number_index//3 - R_index//3) + abs(number_index%3 - R_index%3)
            if (distance_L < distance_R) or (distance_L == distance_R and hand == 'left'):
                L = number
                answer += "L"
            elif (distance_L > distance_R) or (distance_L == distance_R and hand == 'right'):
                R = number
                answer += "R"
    return answer