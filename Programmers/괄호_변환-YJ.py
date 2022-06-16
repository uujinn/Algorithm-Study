def divide(w):
    left_cnt = 0
    right_cnt = 0

    for i in range(len(w)):
        if w[i] == '(':
            left_cnt += 1
        else:
            right_cnt += 1

        if left_cnt == right_cnt:
            return w[:i+1], w[i+1:]  # u, v


def isRight(u):  # 올바른 괄호 문자열 check
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(w):
    # 1
    if not w:
        return ""

    # 2
    u, v = divide(w)

    # 3
    if isRight(u):
        return u + solution(v)

    # 4
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for i in u[1:len(u) - 1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('

        return answer
