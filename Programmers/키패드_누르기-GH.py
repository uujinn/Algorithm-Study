def position(num, left, right, hand):
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    # (x1, y1), (x2, y2) 의 거리: |x1-x2| + |y1-y2|
    dist_L = abs(keypad[num][0] - keypad[left][0]) + abs(keypad[num][1] - keypad[left][1])
    dist_R = abs(keypad[num][0] - keypad[right][0]) + abs(keypad[num][1] - keypad[right][1])
    
    if dist_R > dist_L:     # 왼손이 더 가까우면
        return 'L'
    elif dist_R < dist_L:   # 오른손이 더 가까우면
        return 'R'
    else:                   # 거리가 같으면
        if hand == 'right': # 오른손잡이 = R
            return 'R'
        else:
            return 'L'      # 왼손잡이 = L
        

def solution(nums, hand):
    result = ''
    
    # 왼손 엄지는 *, 오른손 엄지는 #으로 초기화
    left = '*'
    right = '#'
    
    for num in nums:
        if num in [1, 4, 7]:    # 1, 4, 7 -> 왼손 엄지
            result += 'L'
            left = num
        elif num in [3, 6, 9]:  # 3, 6, 9 -> 오른손 엄지
            result += 'R'
            right = num
        else:           # 2, 5, 8, 0일 경우
            center = position(num, left, right, hand)
            result += center
            if center == 'R':
                right = num
            else:
                left = num
                
    return result