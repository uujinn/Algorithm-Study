temp = '124'

def convert(num, base):
    q, r = divmod(num - 1, base)

    if q == 0:
        return temp[r]
    return convert(q, base) + temp[r]


def solution(n):    
    return convert(n, 3)