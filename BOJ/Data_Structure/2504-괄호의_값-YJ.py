from sys import stdin

def check_valid(string): # 올바른 괄호열 check
    stack = []
    for s in string:
        # print(stack)
        if s == '(' or s == '[': # 괄호 시작이면
            stack.append(s) # 스택에 넣어줌
        elif s == ')':
            if not stack: # 스택이 비어있다면 False
                return False
            if stack[-1] == '(':
                stack.pop()
            else: # 짝이 맞지 않다면 False
                return False
        elif s == ']':
            if not stack: # 스택이 비어있다면 False
                return False
            if stack[-1] == '[': 
                stack.pop()
            else: # 짝이 맞지 않다면 False
                return False
    return False if stack else True


def calc(string): # 계산
    stack = []
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                tmp = 0 # 중간계산을 위한 tmp
                for i in reversed(range(len(stack))): # 스택 위에서부터 '(' 찾음
                    # print(tmp)
                    if stack[i] == '(':
                        stack[-1] = 2 * tmp
                        break
                    else: # 올바른 문자열이므로 '(' 없으면 계속 더해주면 됨 X+Y
                        tmp += stack[i]
                        stack.pop()
        elif s == ']': # 같은 원리
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                tmp = 0 
                for i in reversed(range(len(stack))): 
                    # print(tmp)
                    if stack[i] == '[':
                        stack[-1] = 3 * tmp
                        break
                    else: 
                        tmp += stack[i]
                        stack.pop()
    
    return sum(stack)

# main
string = stdin.readline().rstrip()

if check_valid(string):
    print(calc(string))
else:
    print(0)