from sys import stdin
N = int(stdin.readline())
expression = str(stdin.readline().rstrip())
answer = ""
temp = []
temp_num = {}
for i in range(N):
    temp_num[chr(i + 65)] = str(stdin.readline().rstrip())

for i in range(len(expression)-1, -1, -1):
    if not expression[i].isalpha(): #연산자
        temp.append(expression[i])
    else:
        answer += temp_num[expression[i]]
        if temp:
            answer += temp.pop()

print('%0.2f'%(eval(answer[::-1])))