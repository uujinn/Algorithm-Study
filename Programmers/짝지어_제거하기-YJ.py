def solution(s):

    if len(s) % 2 == 1:  # 홀수일 경우
        return 0

    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0


print(solution('baabaa'))
