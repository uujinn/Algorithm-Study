equation = input()
stack = []
answer = ''

for x in equation:
    if x.isalpha():
        answer += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x =='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                answer += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()

# 스택 안에 값이 있을 때 stack.pop()          
while stack:
    answer += stack.pop()
print(answer)