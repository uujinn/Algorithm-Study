def solution(x):
    hap = sum([int(s) for s in str(x)])
    return True if hap != 0 and x % hap == 0 else False