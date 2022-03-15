import sys

stack = []

for i in range(int(sys.stdin.readline())):
    str = sys.stdin.readline().rstrip()
    
    if 'push' in str:
        _, n = str.split()
        stack.append(n)
    elif 'pop' in str:
        print(stack.pop()) if stack else print(-1)
    elif str == 'size':
        print(len(stack))
    elif str == 'empty':
        print(0) if stack else print(1)
    elif str == 'top':
        print(stack[-1]) if stack else print(-1)