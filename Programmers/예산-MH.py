def solution(d, budget):
    answer = 0

    for i in sorted(d):
        if budget >= i:
            budget -= i
            answer += 1
        else:
            return answer

    return answer

print(solution([1,3,2,5,4],	9))