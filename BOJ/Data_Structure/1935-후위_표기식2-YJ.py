from sys import stdin

N = int(stdin.readline())
expression = stdin.readline().rstrip() # 후위 표기식
numbers = [0] * N # 알파벳에 대응하는 숫자
stack = [] # 계산에 사용할 스택


for i in range(N):
    numbers[i] = int(stdin.readline().rstrip())

for n in expression:
    
    if 'A' <= n <= 'Z':
        stack.append(numbers[ord(n)-ord('A')]) # 알파벳이면 stack에 해당 숫자로 변환해서 넣어줌
    else: # 연산자라면 계산
        second = stack.pop()
        first = stack.pop()

        if n == '+':
            stack.append(first + second)
        elif n == '-':
            stack.append(first - second)
        elif n == '*':
            stack.append(first*second)
        elif n == '/':
            stack.append(first/second)

print(f'{stack.pop():.2f}') # 소수점 자리 맞춰서 출력