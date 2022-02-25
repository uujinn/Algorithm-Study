def solution(d, budget):
    tmp = 0
    for i, D in enumerate(sorted(d)):
        tmp += D
        if tmp > budget: return i
        elif tmp == budget: return i+1
    return len(d)