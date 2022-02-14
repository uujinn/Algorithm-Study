import sys
input = sys.stdin.readline

x = list(input())
stack = []
error = 1 

for i in x:
    if i == "(":
        stack.append(i)
        cnt = 0
        
    elif i == ")":
        num = 0
        while len(stack) != 0:
            a = stack.pop()
            if a == "(":
                if cnt == 0:  # ()일 때
                    stack.append(2)
                    cnt = 1
                    error = 0   
                else:
                    stack.append(num * 2)
                    cnt = 1
                    error = 0
                break    
            elif a == '[':
                print(0)
                exit(0)
            else:   # 숫자이면        
                num += a
                error = 1
        if error == 1:
            print(0)
            exit(0)
    elif i == "[":
        stack.append(i)
        cnt = 0
    elif i == "]":
        num = 0
        while len(stack) != 0:
            
            a = stack.pop()
            if a == "[":
                if cnt == 0:  # ()일 경우
                    stack.append(3)
                    cnt = 1
                else:
                    stack.append(num * 3)
                    cnt = 1
                error = 0
                break    
            
            elif a == '(':
                print(0)
                exit(0)
                
            else:   # 숫자일 경우
                num += a
                error = 1
                
        if error == 1:
            print(0)
            exit(0)    
answer = 0   

for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        answer += i
print(answer)