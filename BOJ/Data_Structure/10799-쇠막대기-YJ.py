from sys import stdin

expression = stdin.readline().rstrip()
sticks = 0
result = 0

index = 0

for c in expression:
    if c == "(":
        if expression[index+1] == ")": # 레이저라면
            result += sticks
        else: # 막대기 추가
            sticks += 1
    else:
        if expression[index-1] == "(": # 레이저였다면
            pass
        else: # 막대기 끝남
            sticks -= 1
            result += 1

    index += 1

print(result)