from sys import stdin

stack, temp, answer = [], 1, 0
dict = {'(' : 2, ')' : 2, '[' : 3, ']' : 3}

bracket = stdin.readline().rstrip()

for i in range(len(bracket)):
    if bracket[i] in '([':
        temp *= dict[bracket[i]]
        stack.append(bracket[i])
    
    elif bracket[i] in ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if bracket[i - 1] =='(':
            answer += temp
        temp //= 2
        stack.pop()
        
    elif bracket[i] in ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if bracket[i - 1] =='[':
            answer += temp
        temp //= 3
        stack.pop()

if stack:
    answer = 0
print(answer)

# 72ms