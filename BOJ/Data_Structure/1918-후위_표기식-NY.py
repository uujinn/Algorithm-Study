from sys import stdin
S = str(stdin.readline().rstrip())
stack = []
answer = ""
for s in S:
    if s.isalpha():
        answer += s
    else:
        if s == '(':
            stack.append(s)
        elif s in '*/':
            while stack and (stack[-1] in '*/'): #다시 곱셈이나 나눗셈 만날때까지 pop
                answer += stack.pop()
            stack.append(s)
        elif s in '+-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()

while stack:
    answer += stack.pop()

print(answer)