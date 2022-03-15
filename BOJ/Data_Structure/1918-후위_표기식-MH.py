from sys import stdin

stack = []
notation = stdin.readline().rstrip()       # 중위 표기식
answer = ''

for n in notation:    
    if n.isalpha():
        answer += n
        
    elif n == '(':
        stack.append(n)
        
    elif n == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
        
    elif n in '*/':
        while stack and stack[-1] in '*/':
            answer += stack.pop()
        stack.append(n)
        
    elif n in '+-':
        while stack and (stack[-1] != '(' or stack[-1] in '*/+-'):
            answer += stack.pop()
        stack.append(n)
    
while stack:
    answer += stack.pop()
    
print(answer)

# 72ms