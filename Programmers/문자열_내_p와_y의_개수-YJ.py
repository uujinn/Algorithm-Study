def solution(s):

    s = s.lower()
    p = s.count('p')
    y = s.count('y')

    if p == y:
        return True
    else:
        return False
