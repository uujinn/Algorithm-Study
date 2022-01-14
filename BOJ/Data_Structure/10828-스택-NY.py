from sys import stdin
N = int(stdin.readline())
stack = []

for i in range(N):
    commands = str(stdin.readline().rstrip()) #rstrip()이라는 함수를 사용하면 자동으로 개행 문자를 삭제함
    #입력 받은 commands에 빈칸이 있으면 split. 
    try:
        COMMAND, NUM = commands.split()
    except:
        COMMAND = commands
        
    if COMMAND == 'push':
        stack.append(NUM)
    elif COMMAND == 'top':
        print(stack[-1] if len(stack) > 0 else -1)
    elif COMMAND == 'size':
        print(len(stack))
    elif COMMAND == 'pop':
        print(stack.pop() if len(stack) > 0 else -1)
    elif COMMAND == 'empty':
        print(1 if len(stack) == 0 else 0)
