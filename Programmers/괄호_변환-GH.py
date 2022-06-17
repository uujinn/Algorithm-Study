from collections import deque


def check(p):
    stack = deque([])
    for tmp in p:
        if tmp == '(':
            stack.append(tmp)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True


def solution(p):

    if check(p):
        return p

    i = 0
    cnt, cnt_ = 0, 0
    while True:
        if p[i] == '(':
            cnt += 1
        else:
            cnt_ += 1
        i += 1
        if cnt == cnt_:
            break

    u = p[:i]
    v = p[i:]

    if check(u):
        return u + solution(v)
    else:
        result = '(' + solution(v) + ')'
        u = u[1:-1]
        for tmp in u:
            if tmp == '(':
                result += ')'
            else:
                result += '('
        return result