myList = list(input())
answer = 0
stack = []

for i in range(len(myList)):
    if myList[i] == '(':    # 스택에 넣기
        stack.append('(')
        
    else:
        if myList[i-1] == '(':  # ()의 경우면 (를 pop 하고 현재 스택에 있는 ( 개수 만큼 더해 줌
            stack.pop()
            answer += len(stack)
            
        else:
            stack.pop() 
            answer += 1 # 막대기 끝 부분 더해 줌

print(answer)