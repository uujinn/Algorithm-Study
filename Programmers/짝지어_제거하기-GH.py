def solution(s):
    answer = 0 if delete(s) else 1
    return answer

def delete(s):
    stack = []
    for x in s:
        if not stack:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
    return stack