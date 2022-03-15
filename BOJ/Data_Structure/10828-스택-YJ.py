from sys import stdin

N = int(stdin.readline())

# 리스트를 스택으로 사용
stack = []

for i in range(N):
    command = stdin.readline().split()

    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1 if len(stack)==0 else 0)
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    