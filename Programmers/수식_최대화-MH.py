from itertools import permutations

def solution(expression):
    symbol = ['+', '-', '*']
    answer = []
    
    for per in permutations(symbol):
        third, second = per[0], per[1]               # 세번째 우선순위 연산자, 두번째 우선순위 연산자 저장 (제일 우선순위 연산자는 괄호로 처리)
        list = []
        
        for e in expression.split(third):                   # 세번째 우선순위 연산자로 split
            temp = [f"({i})" for i in e.split(second)]      # 두번째 우선순위 연산자로 split 후 괄호(제일 우선순위)로 묶음
            list.append(f'({second.join(temp)})')           # 괄호 묶은 수식을 두번째 우선순위 연산자로 join
            # temp : ['(100)', '(200*300)', '(500)']
            # list : ['((100)-(200*300)-(500))']

        answer.append(abs(eval(third.join(list))))          # 세번째 우선순위 연산자로 join, eval 통해 계산, 절댓값
        # ((100)-(200*300)-(500))+((20))

    return max(answer)

print(solution("100-200*300-500+20"))