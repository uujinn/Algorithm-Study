import enum
from sys import stdin
brackets = str(stdin.readline().rstrip())
stack = [brackets[0]] #첫 괄호를 무조건 넣고 시작
if brackets[0] in ')]': brackets = "" #만약 첫 괄호가 닫는 괄호라면 무조건 틀린 괄호임. brackets을 지워서 for문을 돌지 않도록 조정
number = {'[':'3', '(':'2', ']':'3', ')':'2'}
popped, pop_cnt, app_cnt = False, 0, 1 #바로 직전에 popped 유무에 따라 더해주는 문자가 달라짐. pop_cnt와 app_cnt는 pop과 append 한 횟수가 같아야 괄호들이 쌍을 잘 이룬것이기 때문에 추가함.
exp = "" #마지막에 eval에 사용될 식

for i in range(1, len(brackets)):
    if brackets[i] in '([': #여는 괄호일때
        if not popped: #그 전에 닫는 괄호가 아니었음
            exp += (number[brackets[i-1]]+'*(')
        else: #그 전에 닫는 괄호였음
            exp += '+'
            popped = False
        stack.append(brackets[i])
        app_cnt += 1
    else:
        if not stack or stack[-1]+brackets[i] == '(]' or stack[-1]+brackets[i] == '[)': #잘못된 경우
            exp = '0'
            break
        
        if not popped: 
            exp += number[brackets[i]]
        else: #바로 직전에 popped 됐음. 
            exp += ')'
        stack.pop()
        pop_cnt += 1
        popped = True
            

if stack or app_cnt != pop_cnt:
    exp = '0'

print(eval(exp))