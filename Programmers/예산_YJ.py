def solution(d, budget):
    answer = 0
    d.sort()

    for i in range(len(d)):
        if sum(d[:i+1]) <= budget:
            answer += 1
        else:
            break

    return answer