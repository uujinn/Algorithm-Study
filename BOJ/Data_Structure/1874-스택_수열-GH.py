import sys
input = sys.stdin.readline
 
n = int(input())
tgs = [int(input()) for _ in range(n)]
 
flag = True
stack, answer, current = [], [], 0
 
for tg in tgs:
    while True:
        if stack and stack[-1] == tg:
            answer.append('-')
            stack.pop()
            break
 
        elif current > tg:
            flag = False
 
        else:
            current += 1
            stack.append(current)
            answer.append('+')
 
        if not flag:
            print('NO')
            exit()
 
if flag:
    print('\n'.join(answer))