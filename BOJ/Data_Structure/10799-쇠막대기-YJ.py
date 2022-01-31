from sys import stdin

expression = stdin.readline().rstrip()
sticks = 0 # 갖고 있는 막대기 갯수
result = 0 

index = 0 # 인덱스

for c in expression:
    if c == "(":
        if expression[index+1] == ")": # 레이저라면
            result += sticks # 막대기 갯수대로 + 됨
        else: # 막대기 추가
            sticks += 1
    else:
        if expression[index-1] == "(": # 레이저였다면
            pass
        else: # 막대기 처리 끝남
            sticks -= 1
            result += 1 # 막대기 끄트머리 마무리

    index += 1

print(result)