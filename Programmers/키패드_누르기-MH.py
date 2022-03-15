from glob import glob

answer = ''
left_curr = -1
right_curr = -2
numpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -2]]

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def solution(numbers, hand):
    global answer, left_curr, right_curr, numpad

    for i in numbers:
        pos = getPosition(i)
        if pos.x == 0:  # left
            setCurr(True, i)
        elif pos.x == 2:
            setCurr(False, i)
        elif pos.x == 1:
            left_dis = getDistance(getPosition(left_curr), pos)
            right_dis = getDistance(getPosition(right_curr), pos)

            if(left_dis < right_dis):
                setCurr(True, i)
            elif(right_dis < left_dis):
                setCurr(False, i)
            else:
                setCurr(hand == 'left', i)

    return answer


def getDistance(startPos, targetPos):
    return abs(startPos.x - targetPos.x) + abs(startPos.y - targetPos.y)


def getPosition(number):
    y = 0
    for row in numpad:
        x = 0
        for cal in numpad[y]:
            if number == cal:
                return Position(x, y)
            x += 1
        y += 1


def setCurr(is_left, num):
    global answer, left_curr, right_curr

    if is_left:
        left_curr = num
        answer += 'L'
    else:
        right_curr = num
        answer += 'R'


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
print(solution(numbers, 'right'))