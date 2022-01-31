from sys import stdin

expression = stdin.readline().rstrip()
sticks = [] # 막대기 담아놓을 스택
result = 0

for i in range(len(expression)):
    if expression[i] == "(": # Case1: 레이저 Case2: 새로운 막대기
        if expression[i+1] == ")": # Case 1: 담아져 있는 막대기 갯수 + 1 (레이저가 막대기 자름)
            sticks = list(map(lambda x: x + 1, sticks))
        else: # Case2: 처리 할 막대기 추가
            sticks.append(i)    
    elif expression[i] == ")": 
        if expression[i-1] == "(": # 레이저였다면
            pass   
        elif sticks: # 해당 막대기 처리 끝남
            result += sticks.pop() # 막대기 갯수 계산


print(result)