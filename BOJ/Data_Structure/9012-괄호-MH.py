def checkVPS(str):
    stack = []
    
    for i in range(len(str)):
        if str[i] == '(':
            stack.append('.')
        elif str[i] == ')':
            if len(stack) == 0:
                print('NO')
                return
            else:
                stack.pop()
            
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
    
num = int(input())
for i in range(num):
    str = input()
    checkVPS(str)