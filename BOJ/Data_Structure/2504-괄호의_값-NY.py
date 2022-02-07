import enum
from sys import stdin
brackets = str(stdin.readline().rstrip())
stack = [brackets[0]]
number = {'[':'3', '(':'2', ']':'3', ')':'2'}
popped = False
exp = ""

for i in range(1, len(brackets)):
    if brackets[i] in '([':
        if not popped:
            exp += (number[brackets[i-1]]+'*(')
        else:
            exp += '+'
            popped = False
        stack.append(brackets[i])
    else:
        if stack[-1]+brackets[i] == '(]' or stack[-1]+brackets[i] == '[)':
            exp = '0'
            break
        
        if not popped:
            exp += number[brackets[i]]
        else:
            exp += ')'
        stack.pop()
        popped = True
            

if stack:
    exp = '0'

print(eval(exp))