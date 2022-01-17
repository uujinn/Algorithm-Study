N = int(input())
stack = []

for _ in range(N):
    stack.clear()
    flag = 0
    line = input()
    
    for ps in line:
        if ps == "(":
            stack.append(ps)
        else:
            try:
                stack.pop()
            except: # 예외 처리
                flag = 1
                break
    
    if len(stack) == 0 and flag == 0:
        print("YES")
    else:
        print("NO")