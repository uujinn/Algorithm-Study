def getDistance(A, B): # 거리 계산
    return abs(A[0]-B[0]) + abs(A[1]-B[1])

def solution(numbers, hand): # hand =  right, left
    answer = ''

    # 번호마다 위치 할당
    location = {1:(0, 0), 2:(0, 1), 3:(0, 2),
                4:(1, 0), 5:(1, 1), 6:(1, 2),
                7:(2, 0), 8:(2, 1), 9:(2, 2),
                '*':(3, 0), 0:(3, 1), '#':(3, 2)}
    
    left,right = '*','#'

    for number in numbers:
        if number in [1,4,7]: # 왼손
            answer += 'L'
            left = number
        elif number in [3,6,9]: # 오른손
            answer += 'R'
            right = number
        elif number in [2,5,8,0]: # 거리에 따라 다름
            if getDistance(location[left], location[number]) < getDistance(location[right], location[number]):
                answer += 'L'
                left = number
            elif getDistance(location[left], location[number]) > getDistance(location[right], location[number]):
                answer += 'R'
                right = number
            else:
                if hand == "left":
                    answer += 'L'
                    left = number
                else:
                    answer += 'R'
                    right = number

    return answer