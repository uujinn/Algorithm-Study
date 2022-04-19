import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    
    pattern = re.compile('(\d+)([SDT])([*#]?)')
    answer = pattern.findall(dartResult)
    # [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')] 형식의 answer

    for i in range(len(answer)):
        if answer[i][2] == '*' and i > 0:
            answer[i - 1] *= 2
        answer[i] = int(answer[i][0]) ** bonus[answer[i][1]] * option[answer[i][2]]

    return sum(answer)

print(solution('1S2D*3T'))