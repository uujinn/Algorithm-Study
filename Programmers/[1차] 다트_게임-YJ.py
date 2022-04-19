'''
당첨 시 S: 1제곱 D: 2제곱 T: 3제곱
*: 해당 점수와 바로 전에 얻은 점수를 각각 2배 -> 첫번째 기회에서도 나올 수 O 
#: 해당 점수는 마이너스
*랑 # 효과 중첩 가능 (#의 점수 -2배)
'''

def solution(dartResult):
    stack = []
    points = {'S': 1, 'D': 2, 'T': 3}
    tmp = ''
    for val in dartResult:
        if val.isnumeric(): 
            tmp += val 
            # print(val)       
        elif val in points:
            stack.append(int(tmp)**points[val])
            tmp = ''
        elif val == '#':
            stack[-1] = stack[-1] * -1
        elif val == '*':
            stack[-1] = stack[-1] * 2
            if len(stack) >= 2: # 전에 얻은 점수까지
                stack[-2] = stack[-2] * 2

    # print(stack)
    return sum(stack)
