from sys import stdin

# 연산자 우선순위
def check_priority(s):
    if s == '(' or s == ')': return 0
    elif s == '+' or s == '-': return 1
    elif s == '*' or s == '/': return 2
    else: return -1

expression = stdin.readline().rstrip()
stack = []
answer = ""

for s in expression:
    if s == '(': 
        stack.append(s)
    elif s == ')': # '(' 나올 때까지 answer에 더해줌
        while stack:
            tmp = stack.pop()
            if tmp == '(':  break
            else:   
                answer += tmp
    elif s in '+-*/':
        while stack:
            tmp = stack[-1]
            if check_priority(s) <= check_priority(tmp): # 우선순위 확인
                answer += stack.pop()
            else:   break
        stack.append(s)
    else: # 알파벳이면 answer에 더해줌
        answer += s

while stack: # 남아있는 연산자 출력
    answer += stack.pop()


print(answer)
