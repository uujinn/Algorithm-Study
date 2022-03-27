def solution(s):
    p, y = 0, 0
    for word in s:
        if word in ['p', 'P']: p += 1
        elif word in ['y', 'Y']: y += 1
    return True if p==y else False