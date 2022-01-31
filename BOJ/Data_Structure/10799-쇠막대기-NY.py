from sys import stdin
brackets = str(stdin.readline().rstrip())

temp_stack = []
cnt = 0

for i in range(len(brackets)):
    if brackets[i] == '(':
        temp_stack.append('(')
    else: #bracket == ')'
        temp_stack.pop()
        if brackets[i-1] == '(': cnt += len(temp_stack)
        else: cnt += 1
        
print(cnt)